#!/usr/bin/env python3
"""Check the built site's navigability and deployable public-file boundary."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json, sys

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT/'dist'
EXPECTED = {'allyfast','allyfastlite','allymetronome','allymetronomelite','allyclock','allypiano','allystation','alexfighters','allyscore','allyscores'}
LEGACY = {'customer-support/index.html','privacy-policy/index.html','allymetronomelite/support/index.html','allymetronomelite/privacy/index.html'}

class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.refs=[];self.ids=[];self.h1=0;self.main=0;self.title='';self.in_title=False;self.description='';self.missing_alt=0;self.lang=None
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
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
        if tag=='title':self.in_title=False
    def handle_data(self,data):
        if self.in_title:self.title+=data

def check():
    errors=[]
    paths={p.relative_to(PUBLIC).as_posix():p for p in PUBLIC.rglob('*.html')}
    required={'index.html','support/index.html','privacy/index.html'}|LEGACY
    required|={f'{slug}/{tail}index.html' for slug in EXPECTED for tail in ('','support/','privacy/')}
    if set(paths)!=required:errors.append(f'Route mismatch: missing={required-set(paths)}, extra={set(paths)-required}')
    parsed={}
    for name,path in paths.items():
        page=Page();page.feed(path.read_text());parsed[path.resolve()]=page
        if page.h1!=1 or page.main!=1:errors.append(f'{name}: expected one h1 and main')
        if page.lang!='en' or not page.title.strip() or not page.description.strip():errors.append(f'{name}: missing metadata')
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
    print(f'PASS: {len(paths)} pages, {links} local references, ten complete app page sets, metadata, accessible landmarks, legacy routes, and public-only packaging.')
    print(f'{len(external)} external HTTPS destinations found.')
    return 0
if __name__=='__main__':sys.exit(check())
