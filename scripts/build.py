#!/usr/bin/env python3
"""Generate a portable, dependency-free static app showcase."""
from pathlib import Path
import html, json, os, shutil, struct, sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from site_content import APPS, BY_SLUG, SUPPORT_EMAIL, SITE_URL, SHARE_IMAGE, SHARE_IMAGE_ALT
ROOT = Path(__file__).resolve().parents[1]
PAGES = []

def esc(value): return html.escape(str(value), quote=True)
def href(route, target=''):
    folder = ROOT / route
    dest = ROOT / target
    result = os.path.relpath(dest, folder).replace(os.sep, '/')
    if not Path(target).suffix: result += '/'
    return result

def image(route, source, alt='', cls='', eager=False):
    return f'<img class="{cls}" src="{href(route,source)}" alt="{esc(alt)}" loading="{"eager" if eager else "lazy"}" decoding="async">'

def icon(route, app, cls='app-icon'):
    return image(route, app['icon'], '', cls)

def action(route, app):
    links=[]
    if app.get('store'): links.append(f'<a class="button primary" href="{esc(app["store"])}">Get on the App Store <span aria-hidden="true">↗</span></a>')
    if app.get('web'):
        label='Play the demo' if app['slug']=='alexfighters' else 'Open web app'
        links.append(f'<a class="button {"secondary" if links else "primary"}" href="{esc(app["web"])}">{label} <span aria-hidden="true">↗</span></a>')
    if not links: links.append(f'<a class="button secondary" href="{href(route,app["slug"]+"/support")}">Contact the developer <span aria-hidden="true">↗</span></a>')
    return ''.join(links)

def shell(route,title,description,body,active='apps'):
    home=href(route)
    page_title=f'{title} | AllyWorld' if route else 'AllyWorld | Apps for everyday, music and play'
    page_url=SITE_URL+(route+'/' if route else '')
    share_url=SITE_URL+SHARE_IMAGE
    with (ROOT/SHARE_IMAGE).open('rb') as preview:
        header=preview.read(24)
    if header[:8]!=b'\x89PNG\r\n\x1a\n': raise ValueError('Social preview must be a PNG image')
    share_width,share_height=struct.unpack('>II',header[16:24])
    nav=lambda label,url,key: f'<a href="{url}"'+(' aria-current="page"' if active==key else '')+f'>{label}</a>'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(page_title)}</title><meta name="description" content="{esc(description)}">
<meta name="theme-color" content="#ffffff"><link rel="canonical" href="{esc(page_url)}">
<meta property="og:title" content="{esc(page_title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:type" content="website"><meta property="og:site_name" content="AllyWorld"><meta property="og:locale" content="en_US"><meta property="og:url" content="{esc(page_url)}">
<meta property="og:image" content="{esc(share_url)}"><meta property="og:image:secure_url" content="{esc(share_url)}"><meta property="og:image:type" content="image/png"><meta property="og:image:width" content="{share_width}"><meta property="og:image:height" content="{share_height}"><meta property="og:image:alt" content="{esc(SHARE_IMAGE_ALT)}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(page_title)}"><meta name="twitter:description" content="{esc(description)}"><meta name="twitter:image" content="{esc(share_url)}"><meta name="twitter:image:alt" content="{esc(SHARE_IMAGE_ALT)}">
<link rel="icon" href="{href(route,'assets/favicon.svg')}" type="image/svg+xml"><link rel="stylesheet" href="{href(route,'assets/site.css')}">
</head><body><a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="container header-inner"><a class="wordmark" href="{home}" aria-label="AllyWorld home"><span class="brand-mark" aria-hidden="true">a.</span>AllyWorld</a>
<nav aria-label="Main navigation">{nav('Our apps',home+'#apps','apps')}{nav('Support',href(route,'support'),'support')}{nav('About',home+'#about','about')}</nav><a class="header-contact" href="mailto:{SUPPORT_EMAIL}">Say hello <span aria-hidden="true">↗</span></a></div></header>
<main id="main">{body}</main>
<footer class="site-footer"><div class="container"><div class="footer-top"><a class="wordmark" href="{home}"><span class="brand-mark" aria-hidden="true">a.</span>AllyWorld</a><p>A little world of apps.<br>Made to be part of yours.</p><div class="footer-links"><a href="{home}#apps">Our apps</a><a href="{href(route,'support')}">Support</a><a href="{href(route,'privacy')}">Privacy</a><a href="mailto:{SUPPORT_EMAIL}">Contact</a></div></div><div class="footer-bottom"><span>© 2026 AllyWorld</span><span>Built with curiosity. Made for you.</span></div></div></footer>
</body></html>'''

def card(route,app):
    return f'''<article class="app-card" style="--app-accent:{app['accent']};--app-tint:{app['tint']}"><div class="card-top">{icon(route,app)}<span class="platform">{esc(app['platform'])}</span></div><h3><a href="{href(route,app['slug'])}">{app['name']}<span aria-hidden="true">↗</span></a></h3><p>{app['summary']}</p><div class="card-bottom"><span class="availability">{app['status']}</span><a href="{href(route,app['slug'])}" aria-label="Explore {app['name']}">Explore <span aria-hidden="true">→</span></a></div></article>'''

def home():
    route='';piano=BY_SLUG['allypiano']; clock=BY_SLUG['allyclock'];metro=BY_SLUG['allymetronome']
    groups=''.join(f'<section class="app-group" aria-labelledby="group-{g.lower()}"><div class="group-heading"><h3 id="group-{g.lower()}">{g}</h3><span>{sub}</span></div><div class="app-grid">'+''.join(card(route,a) for a in APPS if a['group']==g)+'</div></section>' for g,sub in [('Everyday','A little more time for you.'),('Music','Find a rhythm. Follow an idea.'),('Games','A world worth playing in.')])
    body=f'''<section class="hero container"><div class="hero-copy"><p class="eyebrow"><span class="tiny-dot"></span> A LITTLE WORLD OF POSSIBILITIES</p><h1>Make time for<br>what you <span>love.</span></h1><p class="hero-description">Find your focus. Play a few notes. Beat the next boss.<br class="desktop-break"> Meet the apps that make up AllyWorld.</p><div class="actions"><a class="button primary" href="#apps">Explore our apps <span aria-hidden="true">↓</span></a><a class="text-link" href="{href(route,'support')}">Here to help <span aria-hidden="true">↗</span></a></div><div class="hero-note"><span class="tiny-dot"></span> Everyday tools, musical ideas & little adventures.</div></div><div class="hero-showcase" aria-label="Featured AllyWorld apps"><a class="showcase-panel showcase-piano" href="{href(route,'allypiano')}"><div class="showcase-label">{icon(route,piano)}<div><strong>AllyPiano</strong><span>Play a little. Feel a lot.</span></div><span class="panel-arrow" aria-hidden="true">↗</span></div>{image(route,piano['screens'][0],'AllyPiano concert grand keyboard','showcase-screen',True)}</a><a class="showcase-panel showcase-clock" href="{href(route,'allyclock')}"><div class="mini-label">AllyClock <span aria-hidden="true">↗</span></div>{image(route,clock['screens'][0],'AllyClock fullscreen time display','',True)}</a><a class="showcase-panel showcase-metro" href="{href(route,'allymetronome')}"><div class="mini-label">AllyMetronome <span aria-hidden="true">↗</span></div>{image(route,metro['screens'][0],'AllyMetronome app promotional image','',True)}</a><div class="showcase-caption"><span class="tiny-dot"></span> Small things. Thoughtfully made.</div></div></section>
<section class="catalog container" id="apps"><div class="section-heading"><div><p class="eyebrow">THE ALLYWORLD COLLECTION</p><h2>Something for your everyday.<br>Something just for fun.</h2></div><span class="collection-count">10 apps. One world.</span></div>{groups}</section>
<section class="about-band" id="about"><div class="container about-grid"><div><p class="eyebrow">A NOTE FROM ALLYWORLD</p><h2>Useful by nature.<br>Playful at heart.</h2></div><div><p>AllyWorld brings together practical tools, musical instruments, and games. Each app has its own personality and a simple reason to be here: to help you do something you enjoy.</p><p>From a steady beat to a new high score, there’s a little world to explore.</p><a class="text-link" href="mailto:{SUPPORT_EMAIL}">Say hello <span aria-hidden="true">↗</span></a></div></div></section>
<section class="support-callout container"><div><p class="eyebrow">WE’RE HERE TO HELP</p><h2>A question about an app?</h2><p>Find help, privacy information, and a way to reach us.</p></div><a class="button dark" href="{href(route,'support')}">Visit support <span aria-hidden="true">↗</span></a></section>'''
    return shell(route,'Apps for everyday, music & play','Discover AllyWorld apps for fasting, time, music, and games. Find product information, downloads, support, and privacy policies.',body)

def app_page(app):
    route=app['slug']; media=''
    if app['screens']:
        media='<div class="product-gallery">'+''.join(f'<figure>{image(route,s,app["name"]+" screenshot "+str(i+1),"product-screen",i==0)}<figcaption>{"App preview" if app["slug"] in ["allyscore","allyscores"] else "From the app"}</figcaption></figure>' for i,s in enumerate(app['screens']))+'</div>'
    else: media=f'<div class="game-art" style="--app-tint:{app["tint"]}">{image(route,app["icon"],app["name"]+" artwork","",True)}<span>In development</span></div>'
    features=''.join(f'<article><span class="feature-number">0{i+1}</span><h3>{esc(h)}</h3><p>{esc(p)}</p></article>' for i,(h,p) in enumerate(app['features']))
    related=''
    if app.get('related'):
        peer=BY_SLUG[app['related']]
        related=f'<section class="related container"><p class="eyebrow">ALSO IN THE FAMILY</p><a class="related-link" href="{href(route,peer["slug"])}">{icon(route,peer)}<div><h2>{peer["name"]}</h2><p>{peer["tagline"]}</p></div><span aria-hidden="true">→</span></a></section>'
    body=f'''<div class="container breadcrumb"><a href="{href(route)}#apps">All apps</a><span aria-hidden="true">/</span>{app['name']}</div><section class="product-hero container" style="--app-accent:{app['accent']}"><div class="product-title">{icon(route,app,'product-icon')}<div><p class="eyebrow">{app['group']} <span aria-hidden="true">/</span> {app['status']}</p><p class="product-name">{app['name']}</p></div></div><h1>{app['tagline']}</h1><p class="product-summary">{app['summary']}</p><div class="actions">{action(route,app)}</div><p class="product-platform">{app['platform']}</p>{media}</section><section class="features container">{features}</section>{related}<section class="product-help container"><h2>Good to know.</h2><div class="help-links"><a href="{href(route,route+'/support')}"><span>Need a hand?</span><strong>{app['name']} support <span aria-hidden="true">↗</span></strong></a><a href="{href(route,route+'/privacy')}"><span>Your information</span><strong>Privacy policy <span aria-hidden="true">↗</span></strong></a></div></section>'''
    return shell(route,app['name'],app['summary'],body)

def write(route,document):
    path=ROOT/route/'index.html';path.parent.mkdir(parents=True,exist_ok=True);path.write_text(document);PAGES.append(str(path.relative_to(ROOT)))

def support_page(app, route=None):
    route=route or app['slug']+'/support'
    questions=''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in app['faq'])
    email=f'mailto:{SUPPORT_EMAIL}?subject={app["name"]}%20support'
    body=f'<div class="container breadcrumb"><a href="{href(route,app["slug"])}">{app["name"]}</a><span aria-hidden="true">/</span>Support</div><article class="document"><p class="eyebrow">HERE TO HELP</p><h1>{app["name"]} support</h1><p class="document-intro">A little help to get you back to what you enjoy.</p><div class="contact-box"><h2>Talk to us.</h2><p>Email <a href="{email}">{SUPPORT_EMAIL}</a> with your question, feedback, or a bug report.</p><p>For a technical issue, include your app version, device or browser, and the steps that led to the problem. Share screenshots only if you are comfortable with the information they contain.</p></div><h2>Common questions</h2>{questions}<div class="actions">{action(route,app)}</div><p><a href="{href(route,app["slug"]+"/privacy")}">Read the {app["name"]} privacy policy</a></p><p><a href="{href(route,"support")}">Support for another app</a></p></article>'
    return shell(route,app['name']+' Support','Help, frequently asked questions, and contact information for '+app['name']+'.',body,'support')

def privacy_page(app, route=None):
    route=route or app['slug']+'/privacy'
    sections=''.join(f'<h2>{esc(h)}</h2><p>{esc(p)}</p>' for h,p in app['privacy'])
    external=''
    if app.get('store') or app['slug']=='allystation':
        external+='<p>Apple handles App Store downloads, purchases, ratings, and diagnostics you choose to share under <a href="https://www.apple.com/legal/privacy/">Apple’s privacy policy</a> and your device settings. AllyWorld does not receive your payment-card information.</p>'
    if app['slug'] in ['allyscore','allyscores']:
        external+='<p>Google processes information used by the optional Drive connection under <a href="https://policies.google.com/privacy">Google’s privacy policy</a>. You can manage connections in your Google Account.</p>'
    if app['slug']=='alexfighters':
        external+='<p>See <a href="https://itch.io/docs/legal/privacy-policy">itch.io’s privacy policy</a> for information about the service hosting the web demo.</p>'
    body=f'<div class="container breadcrumb"><a href="{href(route,app["slug"])}">{app["name"]}</a><span aria-hidden="true">/</span>Privacy</div><article class="document"><p class="eyebrow">YOUR INFORMATION</p><h1>{app["name"]} privacy policy</h1><p class="document-date">Effective September 20, 2026</p><p>This policy describes how {app["name"]}, published by AllyWorld, handles information in its current app or preview.</p>{sections}<h2>Support messages</h2><p>If you contact us, we receive your email address and the information you choose to send. We use it to respond to your request and understand the issue. Contact us if you want us to remove your support correspondence, subject to any applicable retention obligations.</p><h2>Platforms and external services</h2>{external}<p>When you visit this website or a web app, its hosting provider processes the requests needed to deliver the page, which can include an IP address, requested address, and browser information. This is separate from locally stored app records. The AllyWorld promotional site does not use analytics, advertising, or tracking cookies.</p><h2>Changes and contact</h2><p>We update this page and its effective date when these practices change. For questions about privacy, email <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>.</p><p><a href="{href(route,app["slug"]+"/support")}">{app["name"]} support</a> · <a href="{href(route,"privacy")}">All app privacy policies</a></p></article>'
    return shell(route,app['name']+' Privacy Policy','Privacy practices, local storage, external services, and contact information for '+app['name']+'.',body,'privacy')

def index_page(kind):
    route=kind;is_support=kind=='support'
    title='How can we help?' if is_support else 'Your information. In plain sight.'
    subtitle='Choose your app for help, common questions, and a direct way to contact us.' if is_support else 'Every app is different. Find out how each one handles your information.'
    items=''.join(f'<a class="support-item" href="{href(route,a["slug"]+"/"+kind)}">{icon(route,a)}<div><h2>{a["name"]}</h2><p>{"Help & contact" if is_support else "Privacy policy"}</p></div><span aria-hidden="true">↗</span></a>' for a in APPS)
    body=f'<section class="container support-index"><p class="eyebrow">ALLYWORLD {kind.upper()}</p><h1>{title}</h1><p>{subtitle}</p><div class="support-list">{items}</div><div class="contact-box"><h2>Something else on your mind?</h2><p>Reach us at <a class="text-link" href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>.</p></div></section>'
    if not is_support:
        body+='<article class="document"><h2>About this website</h2><p>The AllyWorld promotional site does not use advertising, analytics, or tracking cookies. Pages and images are served by the hosting provider, which handles ordinary web requests. External App Store, web-app, and game-demo links take you to services with their own privacy practices.</p></article>'
    return shell(route,'Support' if is_support else 'Privacy',subtitle,body,kind)

def build():
    PAGES.clear()
    write('',home())
    for app in APPS:
        write(app['slug'],app_page(app))
        write(app['slug']+'/support',support_page(app))
        write(app['slug']+'/privacy',privacy_page(app))
    write('support',index_page('support'))
    write('privacy',index_page('privacy'))
    write('customer-support',support_page(BY_SLUG['allyfast'],'customer-support'))
    write('privacy-policy',privacy_page(BY_SLUG['allyfast'],'privacy-policy'))
    (ROOT/'docs/generated-pages.json').write_text(json.dumps(PAGES,indent=2)+'\n')
    dist=ROOT/'dist'
    if dist.exists(): shutil.rmtree(dist)
    dist.mkdir()
    for source in [*PAGES,'assets']:
        source_path=ROOT/source; destination=dist/source
        destination.parent.mkdir(parents=True,exist_ok=True)
        if source_path.is_dir(): shutil.copytree(source_path,destination)
        else: shutil.copy2(source_path,destination)
    (dist/'.nojekyll').touch()
    print(f'Built {len(PAGES)} pages and a public-only dist directory.')
if __name__=='__main__': build()
