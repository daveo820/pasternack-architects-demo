# Static page builder for the Irwin G. Pasternack, AIA + Associates concept. Run: python3 build.py
from lib import CFG, img, page, bc, finish
BASE='https://pasternack-architects-demo.vercel.app/'
TEL,TEL_H='+16022792808','(602) 279&#8209;2808'
MAIL='ipasternack@pasternack.net'
DIM='<svg class="dim" viewBox="0 0 48 12" aria-hidden="true"><path d="M1 1v10M47 1v10M1 6h46M1 6l5-3M1 6l5 3M47 6l-5-3M47 6l-5 3"/></svg>'
ORG={"@context":"https://schema.org","@type":"ProfessionalService","additionalType":"https://en.wikipedia.org/wiki/Architecture_firm","name":"Irwin G. Pasternack, AIA + Associates, PC","url":BASE,"telephone":"+1-602-279-2808","faxNumber":"+1-602-277-5978","email":MAIL,
 "foundingDate":"1975","founder":{"@type":"Person","name":"Irwin G. Pasternack","jobTitle":"President, Architect"},
 "address":{"@type":"PostalAddress","streetAddress":"745 East Maryland Avenue, Suite 100","addressLocality":"Phoenix","addressRegion":"AZ","postalCode":"85014","addressCountry":"US"},
 "openingHours":"Mo-Fr 08:00-17:00","areaServed":["Arizona","California","Colorado","Iowa","Montana","Nevada","New Mexico","Oklahoma","Texas","Wyoming"],"image":BASE+"img/bull-sculpture.webp"}
CFG.update(base=BASE,name='Irwin G. Pasternack, AIA + Associates',theme='#142a40',org=ORG,
 fonthead='<link rel="preload" as="font" type="font/woff2" href="fonts/big-shoulders-display-normal-800-latin.woff2" crossorigin><link rel="preload" as="font" type="font/woff2" href="fonts/ibm-plex-sans-normal-400-latin.woff2" crossorigin>',
 icon="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%23142a40'/%3E%3Ctext x='16' y='23' font-family='Impact' font-size='17' text-anchor='middle' fill='%23c8a27a'%3EIGP%3C/text%3E%3C/svg%3E",
 bar='Not the official Pasternack site. Every fact and photo comes from pasternackarchitects.com and is used for this pitch only.',
 nav=[('work.html','Work'),('services.html','Services'),('firm.html','The firm'),('contact.html','Contact')],
 mark='<a class="mark" href="index.html" aria-label="Irwin G. Pasternack, AIA + Associates home"><span class="igp" aria-hidden="true">IGP</span><span class="mk-t"><b>Pasternack</b><small>AIA + Associates &middot; Phoenix</small></span></a>',
 cta='<a class="btn" href="contact.html">Discuss a project</a>',
 foot=f'''<footer class="foot"><div class="wrap">
<div class="titleblock"><div class="tb-cell big"><span>Project</span><b>Yours, next.</b></div><div class="tb-cell"><span>Firm</span>Irwin G. Pasternack, AIA + Associates, PC</div><div class="tb-cell"><span>Office</span>745 East Maryland Avenue, Suite 100<br>Phoenix, AZ 85014</div><div class="tb-cell"><span>Call</span><a href="tel:{TEL}">{TEL_H}</a><br>Fax (602) 277&#8209;5978</div><div class="tb-cell"><span>Email</span><a href="mailto:{MAIL}">{MAIL}</a></div><div class="tb-cell"><span>Hours</span>Mon to Fri, 8am to 5pm</div><div class="tb-cell"><span>Sheet</span>Since 1975</div></div>
<div class="foot-row"><nav aria-label="Footer"><a href="work.html">Work</a><a href="services.html">Services</a><a href="firm.html">The firm</a><a href="contact.html">Contact</a></nav><span>Concept by <a href="https://luminarch.pro">LuminArch</a></span></div></div></footer>''')

page('index.html','Irwin G. Pasternack, AIA + Associates | Phoenix Architects',
 'Phoenix architecture and planning firm since 1975: over 4,270 retail, commercial and industrial projects, plus full development services. Call (602) 279 2808.', f'''
<section class="hero"><div class="wrap hero-grid">
 <div class="hero-copy rv"><p class="kicker">{DIM} Phoenix, Arizona &middot; Since 1975</p>
 <h1><span class="count" data-count="4270">4,270</span><span class="plus">+</span> <span class="h1-t">projects. 6,000 buildings. One Phoenix firm.</span></h1>
 <p class="lede">Irwin G. Pasternack, AIA + Associates designs retail, commercial and industrial architecture, and develops and manages projects of its own.</p>
 <div class="cta"><a class="btn" href="work.html">See the work</a><a class="btn btn--plain" href="contact.html">Discuss a project</a></div></div>
 <figure class="hero-fig rv">{img('bull-sculpture.webp','Estrella Promenade in Phoenix with the Ed Mell bull and rider sculpture in front',eager=True,sizes='(max-width:900px) 100vw, 55vw')}
 <figcaption class="sheet-tag"><span>A&#8209;101</span>Estrella Promenade, 51st Avenue and Baseline, Phoenix</figcaption></figure>
</div></section>

<section class="ten"><div class="wrap ten-grid">
 <div class="ten-num rv"><b>1.1</b><span>million square feet</span></div>
 <div class="rv"><p class="kicker" style="color:var(--sand)">{DIM} Showcase &middot; TEN Distribution Warehouse I</p><h2>Now home to an Amazon distribution center.</h2>
 <p>Completed in 2020 at 83rd Avenue and the I&#8209;10, phase one of the TEN Development was designed by the firm and is managed by Pasternack Properties. Warehouse 2 is in development next door.</p><a class="btn light" href="work.html#developing">What is developing now</a></div>
</div></section>

<section class="disciplines"><div class="wrap">
 <div class="dc-head rv"><p class="kicker">{DIM} What the firm draws</p><h2>Retail centers, tilt panel industrial, offices, restaurants.</h2></div>
 <div class="dc-grid">
  <figure class="d1 rv">{img('retail-tower.webp','Tuscany Village Center retail buildings on Cave Creek Road',sizes='(max-width:900px) 100vw, 45vw')}<figcaption><b>Retail</b>Tuscany Village Center, Cave Creek corridor</figcaption></figure>
  <figure class="d2 rv">{img('industrial.webp','Gilbert Tech II concrete tilt panel industrial building',sizes='(max-width:900px) 100vw, 30vw')}<figcaption><b>Industrial</b>Gilbert Tech II, one of well over 1,000 tilt panel buildings</figcaption></figure>
  <figure class="d3 rv">{img('arch-facade.webp','Sapporo restaurant with sloped roofs and stone accents',sizes='(max-width:900px) 100vw, 30vw')}<figcaption><b>Restaurant</b>Sapporo</figcaption></figure>
  <figure class="d4 rv">{img('office-courtyard.webp','Maryland Professional Office Complex garden courtyard',sizes='(max-width:900px) 100vw, 45vw')}<figcaption><b>Office</b>Maryland Professional Office Complex, the firm&rsquo;s own headquarters</figcaption></figure>
 </div><a class="btn" href="work.html">The full portfolio</a>
</div></section>

<section class="stats"><div class="wrap st-grid">{''.join(f'<div class="stat rv"><b>{n}</b><span>{l}</span></div>' for n,l in [('1975','founded in Phoenix'),('28+','projects developed by Irwin, all designed and managed by the firm'),('10','states where Irwin is a registered architect'),('1,000+','concrete tilt panel industrial buildings designed')])}</div></section>

<section class="develop"><div class="wrap dv-grid">
 <figure class="rv">{img('rendering-silver-springs.webp','Rendering of the Silver Springs shopping center renovation by Ryan Dolinar',sizes='(max-width:900px) 100vw, 55vw')}</figure>
 <div class="rv"><p class="kicker">{DIM} Architect and developer</p><h2>The firm builds for itself, too.</h2><p>In 1978 Irwin Pasternack started developing his first retail project. That experience is offered to investor clients as full development services: site master planning, rezoning, real estate evaluation and contract administration under one roof.</p><a class="btn btn--plain" href="services.html">All services</a></div>
</div></section>''', extra_ld=[bc(('Home',''))])

WORK=[('Estrella Promenade','Phoenix','bull-sculpture.webp','A standalone Walgreens behind the Ed Mell sculpture at the northwest corner of 51st Avenue and Baseline. Stone facing and large overhangs for shade.'),
 ('Living Spaces Furniture','Phoenix','warehouse-interior.webp','A 125,000 square foot showroom and 375,000 square foot distribution center at 67th Avenue and the I&#8209;10, part of the 74 acre Estrella Vista Commerce Center. Clean contemporary concrete tilt panel.'),
 ('Tuscany Village Center','Cave Creek corridor','retail-tower.webp','Five buildings and 40,000 square feet at Desert Willow Parkway and Cave Creek Road, with whimsical architecture and lush landscape.'),
 ('Maryland Professional Office Complex','Phoenix','dusk-retail.webp','A 26,000 square foot garden office complex at 745 East Maryland Avenue, home to the firm and Pasternack Properties.'),
 ('Southern Promenade','Mesa','retail-center.webp','A 16,000 square foot center near Southern Avenue and Higley Road with rich stone columns and deep earth tones.'),
 ('Sapporo','Restaurant','glass-sculpture.webp','Sloped roofs, stone accents, and stainless steel art and sculpture for an evening that doubles as an architectural experience.'),
 ('Gilbert Tech II','Gilbert','industrial.webp','A 100,000 square foot tilt panel complex at San Angelo and Fiesta Boulevards, one of five buildings designed in a similar style.')]
OTHER=['Superstition Promenade, 60,256 square feet at Power and McDowell, Mesa','Pleasant Promenade, 17,000 square feet at 99th Avenue and Beardsley, Peoria','Estrella Commerce Center, 400,000 square feet master planned at 63rd Avenue and Buckeye','The Shops at Dove Valley Ranch, Carefree Highway and Black Mountain Parkway, Cave Creek']
page('work.html','Portfolio of Irwin G. Pasternack, AIA + Associates in Phoenix',
 'Retail centers, tilt panel industrial, offices and restaurants across the Phoenix valley, plus what the firm is developing now. Browse the work, then call us.', f'''
<section class="page-head"><div class="wrap"><p class="kicker rv">{DIM} Work</p><h1 class="rv">Drawn in Phoenix, built across the valley.</h1></div></section>
<section class="work"><div class="wrap">{''.join(f'<article class="wk rv"><figure>{img(i,n,sizes="(max-width:900px) 100vw, 50vw")}</figure><div class="wk-t"><span class="sheet">A&#8209;{201+k}</span><h2>{n}</h2><p class="loc">{l}</p><p>{d}</p></div></article>' for k,(n,l,i,d) in enumerate(WORK))}
<div class="other rv"><h2>Also in the portfolio</h2><ul>{''.join(f'<li>{DIM}<span>{x}</span></li>' for x in OTHER)}</ul></div></div></section>
<section class="developing" id="developing"><div class="wrap"><p class="kicker rv" style="color:var(--sand)">{DIM} Developing now</p><h2 class="rv">On the boards</h2>
<div class="dev-grid"><figure class="rv">{img('rendering-silver-springs.webp','Silver Springs shopping center renovation rendering',sizes='(max-width:900px) 100vw, 50vw')}<figcaption><b>Silver Springs shopping center renovation</b>91st Avenue and Union Hills. Rendering by Ryan Dolinar.</figcaption></figure>
<figure class="rv">{img('rendering-shops.webp','Silver Springs shops rendering',sizes='(max-width:900px) 100vw, 50vw')}<figcaption><b>Silver Springs shops</b>Ground view. Rendering by Ryan Dolinar.</figcaption></figure></div>
<ul class="dev-list rv"><li><b>Tolleson Distribution Center</b>85th Avenue and Van Buren</li><li><b>TEN Distribution Warehouse 2</b>83rd Avenue and the I&#8209;10</li></ul></div></section>''',
 extra_ld=[bc(('Home',''),('Work','work.html'))])

MAIN=['Conceptual and schematic design consultation','Complete architectural design and construction documentation','Landscape architecture','Site master planning','Rezoning services','Real estate evaluation','Structural, mechanical, plumbing, electrical and civil engineering coordination','Contract administration and inspection services']
SUP=['Life cycle cost analysis','Feasibility and value analysis','Energy studies','Project renderings and models','Architectural photography','Full development services for investor clients','Litigation support','Arbitration and mediation','Forensic analysis of construction and design problems','Expert witness services']
page('services.html','Architecture, Planning and Development Services | Pasternack',
 'From schematic design and construction documents to rezoning, master planning and expert witness work. See every service the Pasternack firm offers, then call.', f'''
<section class="page-head"><div class="wrap"><p class="kicker rv">{DIM} Services</p><h1 class="rv">From the first sketch to the courtroom.</h1>
<p class="lede rv">Retail, commercial and industrial work, with added experience in educational, restaurant and government uses. Small tenant improvements up to multi building developments.</p></div></section>
<section class="svc"><div class="wrap sv-grid"><div class="rv"><h2>Main services</h2><ol class="sv-list">{''.join(f'<li>{x}</li>' for x in MAIN)}</ol></div>
<div class="rv"><h2>Supplemental services</h2><ol class="sv-list alt">{''.join(f'<li>{x}</li>' for x in SUP)}</ol></div></div></section>
<section class="pm"><div class="wrap pm-grid rv"><div><p class="kicker" style="color:var(--sand)">{DIM} Project management</p><h2>Thousands of projects of experience behind every schedule.</h2></div><p>Over 4,270 projects and more than 6,000 buildings. That is the experience the firm brings to meeting a project&rsquo;s goals professionally and efficiently.</p></div></section>''',
 extra_ld=[bc(('Home',''),('Services','services.html'))])

TEAM=[('Irwin G. Pasternack, AIA','President, Architect'),('Dick Presto','Associate. Designer, Project Architect and Landscape Architect'),('Steve Sam','Associate. Architectural Project Manager'),('Thomas Brennan, CISSP, CCNA','Associate. Director of Operations'),('Nate Sonoskey','Associate. Project Development Manager, Architect'),('Charles Broadwick','Associate. Architectural Project Manager'),('Ryan Dolinar','Project Architect'),('Carol Pellegrino','Comptroller')]
ORGS=['The American Institute of Architects','The American Arbitration Society','The Construction Specification Institute','The Arizona Society of Architects','University of Arizona College of Architecture Dean&rsquo;s Advisory Council','The International Conference of Shopping Centers','The Dana Cheryl Beitscher Charitable Foundation','The Valley Partnership']
page('firm.html','About the Firm: Irwin G. Pasternack, AIA + Associates, Phoenix',
 'Founded in 1975 on quality design and documentation and personal attention. Meet Irwin Pasternack, AIA, NCARB certificate holder, and the team in Phoenix today.', f'''
<section class="page-head"><div class="wrap"><p class="kicker rv">{DIM} The firm</p><h1 class="rv">Personal attention, prompt production, since 1975.</h1>
<p class="lede rv">The firm was founded on quality design and construction documentation, personal attention and prompt, thorough production of architectural services.</p></div></section>
<section class="irwin"><div class="wrap ir-grid"><div class="ph-portrait rv" role="img" aria-label="Placeholder for a portrait of Irwin Pasternack"><span>Portrait of Irwin<br>(on the current site)</span></div>
<div class="rv"><h2>Irwin G. Pasternack, AIA</h2><p>A registered architect in ten states: Arizona, California, Colorado, Iowa, Montana, Nevada, New Mexico, Oklahoma, Texas and Wyoming, with a National Registration from NCARB.</p>
<p>And a proud member of the Society of American Magicians and the International Brotherhood of Magicians.</p>
<details><summary>Professional affiliations</summary><ul>{''.join(f'<li>{o}</li>' for o in ORGS)}</ul></details></div></div></section>
<section class="team"><div class="wrap"><h2 class="rv">The team</h2><ul class="tm">{''.join(f'<li class="rv"><b>{n}</b><span>{r}</span></li>' for n,r in TEAM)}</ul>
<aside class="memoriam rv"><p class="kicker">In memoriam</p><p><b>Mike Larson</b>, Senior Project Supervisor, worked more than thirty years alongside Irwin and oversaw projects including Discount Tire, Price Club, Superstition Promenade, Estrella Mountain Village and Distribution I at 10 (Amazon). He passed away on October 16, 2020.</p></aside></div></section>''',
 extra_ld=[bc(('Home',''),('The firm','firm.html'))])

page('contact.html','Contact Irwin G. Pasternack, AIA + Associates | Phoenix, AZ',
 'Set up an appointment to discuss your retail, commercial or industrial project. Call (602) 279 2808 or visit 745 East Maryland Avenue, Suite 100 in Phoenix.', f'''
<section class="page-head"><div class="wrap"><p class="kicker rv">{DIM} Contact</p><h1 class="rv">Set up an appointment.</h1></div></section>
<section class="contact"><div class="wrap ct-grid">
<form class="rv" data-demo="Thank you. On the live site this goes to the Pasternack office. (Demo: nothing was sent.)" novalidate>
<div class="fld"><label for="nm">Name</label><input id="nm" name="nm" autocomplete="name" required></div>
<div class="fld"><label for="co">Company</label><input id="co" name="co" autocomplete="organization"></div>
<div class="fld"><label for="em">Email</label><input id="em" name="em" type="email" autocomplete="email" required></div>
<div class="fld"><label for="ty">Project type</label><select id="ty" name="ty"><option>Retail</option><option>Commercial or office</option><option>Industrial</option><option>Restaurant</option><option>Tenant improvement</option><option>Development partnership</option><option>Expert witness or litigation support</option></select></div>
<div class="fld"><label for="msg">About the project</label><textarea id="msg" name="msg"></textarea></div>
<button class="btn" type="submit">Send</button><p class="formmsg" role="status" aria-live="polite"></p></form>
<aside class="rv ct-side"><figure>{img('office-courtyard.webp','The firm&rsquo;s office at the Maryland Professional Office Complex',sizes='(max-width:900px) 100vw, 40vw')}</figure>
<address><b>Our office</b><br>745 East Maryland Avenue, Suite 100<br>Phoenix, AZ 85014</address><p><a href="tel:{TEL}">{TEL_H}</a> &middot; Fax (602) 277&#8209;5978<br><a href="mailto:{MAIL}">{MAIL}</a><br>Monday to Friday, 8am to 5pm</p></aside></div></section>''',
 extra_ld=[bc(('Home',''),('Contact','contact.html'))])

page('404.html','Page Not Found | Irwin G. Pasternack, AIA + Associates Concept',
 'That sheet is missing from the set. Head back to the Pasternack concept home page, browse the portfolio of Phoenix projects, or call the office to talk.', f'''
<section class="page-head"><div class="wrap"><p class="kicker">{DIM} Sheet missing</p><h1>This sheet is not in the set.</h1><a class="btn" href="index.html">Back to the cover sheet</a></div></section>''')
finish(['index.html','work.html','services.html','firm.html','contact.html'])
print('built')
