#!/usr/bin/env python3
"""Check the built site's navigability and deployable public-file boundary."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json, struct, sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from site_content import SITE_URL, SHARE_IMAGE, SHARE_IMAGE_ALT
PUBLIC = ROOT/'dist'
EXPECTED = {'allyfast','allyfastlite','allymetronome','allymetronomelite','allyclock','allypiano','allystation','alexfighters','allyscore','allyscores'}
LEGACY = {'customer-support/index.html','privacy-policy/index.html','allymetronomelite/support/index.html','allymetronomelite/privacy/index.html'}

class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.refs=[];self.ids=[];self.h1=0;self.main=0;self.title='';self.in_title=False;self.description='';self.missing_alt=0;self.lang=None
        self.in_head=False;self.meta={};self.canonical=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='head': self.in_head=True
        if tag=='meta' and self.in_head:
            key=a.get('property') or a.get('name')
            self.meta.setdefault(key,[]).append(a.get('content',''))
        if tag=='link' and a.get('rel')=='canonical' and self.in_head: self.canonical.append(a.get('href',''))
        if tag=='html': self.lang=a.get('lang')
        if tag=='title': self.in_title=True
        if tag=='h1': self.h1+=1
        if tag=='main': self.main+=1
        if tag=='meta' and a.get('name')=='description': self.description=a.get('content','')
        if 'id' in a:self.ids.append(a['id'])
        if tag=='img' and 'alt' not in a:self.missing_alt+=1
        for key in ('href','src'):
            if a.get(key) is not None:self.refs.append(a[key])
    def handle_endtag(self,tag):
        if tag=='head':self.in_head=False
        if tag=='title':self.in_title=False
    def handle_data(self,data):
        if self.in_title:self.title+=data

def check():
    errors=[]
    share_path=PUBLIC/SHARE_IMAGE
    share_size=None
    if not share_path.is_file(): errors.append('Missing public social preview image')
    else:
        with share_path.open('rb') as preview: header=preview.read(24)
        if len(header)!=24 or header[:8]!=b'\x89PNG\r\n\x1a\n': errors.append('Social preview must be a PNG image')
        else:
            share_size=struct.unpack('>II',header[16:24])
            if share_size[0]<600 or share_size[1]<315: errors.append('Social preview is too small for a large card')
        if share_path.stat().st_size>=5_000_000: errors.append('Social preview must be under 5 MB')
        if share_path.read_bytes()!=(ROOT/SHARE_IMAGE).read_bytes(): errors.append('Stale public social preview image')
    paths={p.relative_to(PUBLIC).as_posix():p for p in PUBLIC.rglob('*.html')}
    required={'index.html','support/index.html','privacy/index.html'}|LEGACY
    required|={f'{slug}/{tail}index.html' for slug in EXPECTED for tail in ('','support/','privacy/')}
    if set(paths)!=required:errors.append(f'Route mismatch: missing={required-set(paths)}, extra={set(paths)-required}')
    parsed={}
    for name,path in paths.items():
        page=Page();page.feed(path.read_text());parsed[path.resolve()]=page
        if page.h1!=1 or page.main!=1:errors.append(f'{name}: expected one h1 and main')
        if page.lang!='en' or not page.title.strip() or not page.description.strip():errors.append(f'{name}: missing metadata')
        page_url=SITE_URL+name.removesuffix('index.html')
        share_url=SITE_URL+SHARE_IMAGE
        if page.canonical!=[page_url]: errors.append(f'{name}: incorrect canonical URL')
        social={'og:title':page.title,'og:description':page.description,'og:type':'website','og:site_name':'AllyWorld','og:locale':'en_US','og:url':page_url,'og:image':share_url,'og:image:secure_url':share_url,'og:image:type':'image/png','og:image:alt':SHARE_IMAGE_ALT,'twitter:card':'summary_large_image','twitter:title':page.title,'twitter:description':page.description,'twitter:image':share_url,'twitter:image:alt':SHARE_IMAGE_ALT}
        if share_size: social.update({'og:image:width':str(share_size[0]),'og:image:height':str(share_size[1])})
        for key,value in social.items():
            if page.meta.get(key)!=[value]: errors.append(f'{name}: missing, duplicate, or incorrect {key}')
        if len(page.title)>70 or len(page.description)>200: errors.append(f'{name}: social title or description is too long')
        if len(page.ids)!=len(set(page.ids)):errors.append(f'{name}: duplicate IDs')
        if page.missing_alt:errors.append(f'{name}: missing image alt attribute')
        if path.read_bytes()!=(ROOT/name).read_bytes():errors.append(f'{name}: stale dist content')
        if '[Insert Date]' in path.read_text() or '®' in path.read_text():errors.append(f'{name}: unverified visible claim')
    links=0
    external=set()
    for source,page in parsed.items():
        for ref in page.refs:
            url=urlsplit(ref)
            if url.scheme in ('https','mailto'):
                if url.scheme=='https':external.add(ref)
                continue
            if url.scheme or url.netloc or ref.startswith('/'):
                errors.append(f'{source.relative_to(PUBLIC)}: nonportable or unsafe link {ref}');continue
            target=(source.parent/unquote(url.path)).resolve() if url.path else source
            if not target.is_relative_to(PUBLIC):errors.append(f'Link leaves public output: {ref}');continue
            if target.is_dir():target/='index.html'
            if not target.is_file():errors.append(f'{source.relative_to(PUBLIC)}: missing target {ref}');continue
            links+=1
            if url.fragment and target in parsed and unquote(url.fragment) not in parsed[target].ids:errors.append(f'Missing anchor: {ref}')
    # A private source/configuration file must never enter the upload's public directory.
    for path in PUBLIC.rglob('*'):
        if path.is_file() and (path.name.startswith('.env') or '.git' in path.parts or path.suffix in ('.py','.json','.md')):
            errors.append(f'Unexpected source/config in public output: {path.relative_to(PUBLIC)}')
    if errors:
        print('\n'.join(errors));return 1
    print(f'PASS: {len(paths)} pages, {links} local references, ten complete app page sets, social previews, metadata, accessible landmarks, legacy routes, and public-only packaging.')
    print(f'{len(external)} external HTTPS destinations found.')
    return 0
if __name__=='__main__':sys.exit(check())
