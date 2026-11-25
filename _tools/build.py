"""Builds the Nurtured by Aanchal static site.

Run from the repo root:  python3 _tools/build.py
Content (recipes, posts, shop picks) lives in _tools/content.py.
Photos: drop them in /images with the names in PHOTOS below and rebuild; until then a placeholder shows.
"""
import json, os, html, hashlib
from datetime import date

SITE = "https://nurturedbyaanchal.com"
EMAIL = "nurturedbyaanchal@gmail.com"
IG = "https://www.instagram.com/nurturedbyaanchal/"
YT = "https://www.youtube.com/@NurturedByAanchal"
THREADS = "https://www.threads.net/@nurturedbyaanchal"
AVEE = "https://www.instagram.com/reel/DahF_vBMJ8L/"
SHORT = "1Y15WDU7Q_k"

PHOTOS = {"hero": "images/aanchal-hero.jpg", "about": "images/aanchal-kitchen.jpg",
          "family": "images/aanchal-family.jpg"}

NAV = [("Home", "/"), ("About", "/about/"), ("Recipes", "/recipes/"), ("Deals", "/deals/"), ("Shop", "/shop/"), ("Contact", "/contact/")]

try:
    from content import RECIPES, POSTS, SHOP
except ImportError:
    RECIPES, POSTS, SHOP = [], [], []
from photos import RECIPE_PHOTOS
for _r in RECIPES:
    if RECIPE_PHOTOS.get(_r["slug"]) and not _r.get("image"):
        _r["image"] = RECIPE_PHOTOS[_r["slug"]] + "?w=1200&h=900&fit=crop&crop=entropy&q=80&auto=format"
        _r["credit"] = "Photo via Unsplash"
from recipe_cards import make_all as _make_cards
_make_cards(RECIPES)

def absurl(u):
    return u if u.startswith("http") else SITE + u


def photo(key, alt):
    p = PHOTOS[key]
    if os.path.exists(p):
        return f'<div class="photo"><img src="/{p}" alt="{html.escape(alt)}"></div>'
    return '<div class="photo empty" role="img" aria-label="Photo of Aanchal"><span>AB</span></div>'


CSSV = hashlib.md5(open("assets/site.css","rb").read()).hexdigest()[:8]

def head(title, desc, path, extra=""):
    full = title if path == "/" else (f"{title} | Nurtured by Aanchal" if len(title) <= 42 else title)
    if len(desc) > 160:
        desc = desc[:157].rsplit(" ", 1)[0].rstrip(",.;:") + "..."
    og_img = "" if "og:image" in extra else f'<meta property="og:image" content="{SITE}/images/aanchal-hero.jpg">\n'
    return f"""<!DOCTYPE html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:title" content="{html.escape(full)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Nurtured by Aanchal">
<meta property="og:locale" content="en_CA">
{og_img}<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#666640">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css?v={CSSV}">
{extra}</head>
<body>
"""


def header(path):
    def cur(h):
        return ' aria-current="page"' if (path == h or (h != "/" and path.startswith(h))) else ""
    links = "\n      ".join(f'<a href="{h}"{cur(h)}>{t}</a>' for t, h in NAV)
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="mark" href="/">Nurtured by Aanchal</a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" onclick="var o=this.getAttribute('aria-expanded')==='true';this.setAttribute('aria-expanded',!o);document.body.classList.toggle('nav-open',!o)"><span class="nav-toggle-bars" aria-hidden="true"></span><span class="nav-toggle-label">Menu</span></button>
    <nav class="site-nav" id="site-nav" aria-label="Main">
      {links}
      <a class="btn" href="/work-with-me/">Work with me</a>
    </nav>
  </div>
</header>
<main>
"""


NEWS = f"""<section class="news" id="newsletter">
  <div class="wrap">
    <h2>Get the good stuff</h2>
    <p>Real mom life, straight to your inbox.</p>
    <p>Our weeknight meals, my workout routine, toddler lunchbox ideas and what's actually working in our week.</p>
    <p>To join, email me with "Subscribe" in the subject line and I'll add you. You can unsubscribe any time by replying "Unsubscribe".</p>
    <p><a class="btn" href="mailto:{EMAIL}?subject=Subscribe&amp;body=Hi%20Aanchal%2C%20please%20add%20me%20to%20your%20newsletter.">Subscribe by email</a> <a class="btn btn-ghost-dark" href="/guides/weeknight-dinner-plan.pdf" download>Get the free dinner plan</a></p>
  </div>
</section>
"""


def footer(scripts=""):
    return f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <div>
      <h2>Nurtured by Aanchal</h2>
      <div class="socials">
        <a href="{IG}" rel="noopener">Instagram</a>
        <a href="{YT}" rel="noopener">YouTube</a>
        <a href="{THREADS}" rel="noopener">Threads</a>
      </div>
    </div>
    <div>
      <h4>Vancouver, BC</h4>
      <p><a href="/disclosure/">Disclosure</a></p>
      <p><a href="/privacy/">Privacy policy</a></p>
      <p><a href="/blog/">Blog</a></p>
    </div>
    <div>
      <h4><a href="/contact/">Contact</a></h4>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p>© {date.today().year} Aanchal Bathija</p>
    </div>
  </div>
</footer>
{scripts}</body>
</html>
"""


FOCAL = json.load(open(os.path.join(os.path.dirname(__file__), "focal.json")))
def _focal(body):
    import re as _re
    def fix(m):
        tag = m.group(0); src = _re.search(r'src="([^"?]+)', tag)
        if src and src.group(1) in FOCAL and "object-position" not in tag:
            return tag.replace("<img ", f'<img style="object-position:{FOCAL[src.group(1)]}" ', 1)
        return tag
    return _re.sub(r"<img [^>]*>", fix, body)

def write(path, body):
    body = _focal(body)
    out = path.strip("/")
    if out:
        os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "index.html") if out else "index.html", "w") as f:
        f.write(body)


def page_title(h1, p):
    return f"""<div class="page-title"><div class="wrap"><h1>{h1}</h1><p>{p}</p></div></div>\n"""


IG_SCRIPT = '<script async src="https://www.instagram.com/embed.js"></script>\n'
MOTION_JS = '''<script>
(function(){
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var els = document.querySelectorAll('.reveal');
  if (reduce || !('IntersectionObserver' in window)) { els.forEach(function(e){e.classList.add('in')}); return; }
  var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target);
    e.target.querySelectorAll('[data-count]').forEach(function(n){ var t=parseFloat(n.dataset.count), d=+(n.dataset.dec||0), suf=n.dataset.suffix||'', st=null;
      function f(ts){ if(!st) st=ts; var p=Math.min((ts-st)/1200,1); n.textContent=(t*(1-Math.pow(1-p,3))).toFixed(d)+suf; if(p<1) requestAnimationFrame(f); } requestAnimationFrame(f); }); } }); }, {threshold:.2});
  els.forEach(function(e){ io.observe(e) });
})();
</script>
'''


def ig_embed(url, label):
    return (f'<div class="ig-wrap"><blockquote class="instagram-media" data-instgrm-permalink="{url}" data-instgrm-version="14">'
            f'<a href="{url}" style="display:block;padding:20px">{label}</a></blockquote></div>')


def link_list(items, base):
    return '<ul class="list-links">' + "\n".join(
        f'<li><strong><a href="{base}{i["slug"]}/">{html.escape(i["title"])}</a></strong>{html.escape(i["summary"])}</li>'
        for i in items) + "</ul>"


# ================= HOME =================
from home_story import home_html
PERSON_LD = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "WebSite", "name": "Nurtured by Aanchal", "url": SITE + "/"},
    {"@type": "Person", "name": "Aanchal Bathija", "url": SITE + "/", "image": SITE + "/images/aanchal-hero.jpg",
     "jobTitle": "Content creator", "description": "Working mom in Vancouver sharing motherhood, family life, fitness and South Asian recipes.",
     "address": {"@type": "PostalAddress", "addressLocality": "Vancouver", "addressRegion": "BC", "addressCountry": "CA"},
     "sameAs": [IG, YT, THREADS]}]}) + '</script>\n'

home = head("Nurtured by Aanchal | Working mom, real conversations",
            "Aanchal Bathija is a working mom in Vancouver with 12M+ Reel views, talking motherhood, marriage, feminism and real routines.",
            "/", PERSON_LD) + header("/") + home_html(IG, AVEE, RECIPES, POSTS, photo, NEWS) + footer(MOTION_JS)
write("/", home)

# ================= ABOUT =================
write("/about/", head("About Aanchal", "Aanchal Bathija is a working mom in Vancouver sharing fitness, family life and real routines.", "/about/")
      + header("/about/") + page_title("My story", "A working mom in Vancouver, trying to look after everyone, including herself.")
      + f"""<section><div class="wrap about-grid">
    {photo("about", "Aanchal with her son")}
    <div class="prose">
      <p style="font-size:1.35rem;line-height:1.5">Becoming a mom changed everything, including how much of me was left at the end of the day.</p>
      <p>I'm Aanchal. I work full time in home insurance, and my husband Anuj and I are raising our two-year-old son in Vancouver, in a home full of South Asian food, family and opinions.</p>
      <p>After my son was born, I wanted my health and my time back. I started training again around my workday, and I started sharing it on Instagram as Nurtured by Aanchal.</p>
      <p>Today I talk about postpartum and mom fitness, women's health, marriage and relationships, South Asian family life, travelling as a family and staying motivated when the to-do list never ends.</p>
      <p>I'm not an expert or a doctor. I share what works for me and my family, and I'm honest about what doesn't.</p>
      <div class="mini-gal">
        <img src="/images/album/family-festive.jpg" alt="Aanchal with family at a celebration" loading="lazy">
        <img src="/images/album/lunch.jpg" alt="Aanchal and her son at lunch" loading="lazy">
        <img src="/images/album/cozy-sweater.jpg" alt="Aanchal in a cozy sweater" loading="lazy">
      </div>
      <h2>Find me</h2>
      <p><a href="{IG}" rel="noopener">Instagram @nurturedbyaanchal</a><br><a href="{YT}" rel="noopener">YouTube @NurturedByAanchal</a><br><a href="{THREADS}" rel="noopener">Threads</a></p>
    </div>
  </div></section>
""" + NEWS + footer())

# ================= RECIPES =================
def recipe_grid(items):
    cats = []
    for r in items:
        if r.get("cat") and r["cat"] not in cats:
            cats.append(r["cat"])
    chips = "".join(f'<a class="chip" href="#{c.lower().replace(" ", "-")}">{html.escape(c)}</a>' for c in cats)
    out = f'<nav class="chips" aria-label="Recipe categories">{chips}</nav>'
    for c in cats:
        cards = "".join(
            f'''<a class="r-card" href="/recipes/{r["slug"]}/"><img src="{r["image"]}" alt="{html.escape(r["title"])}" loading="lazy"><span class="r-meta">{r["prep"] + r["cook"]} min · serves {r["servings"]}</span><h3>{html.escape(r["title"])}</h3></a>'''
            for r in items if r.get("cat") == c)
        out += f'<h2 class="r-cat" id="{c.lower().replace(" ", "-")}">{html.escape(c)}</h2><div class="r-grid">{cards}</div>'
    return out

recipes_body = recipe_grid(RECIPES) if RECIPES else """<div class="soon">
      <h3>The first recipes are on their way</h3>
      <p>Each one will have prep and cook times, ingredients, steps and the Reel where I make it.</p>
      <a class="btn" href="#newsletter">Get them by email</a>
    </div>"""
write("/recipes/", head("Recipes", "Weeknight South Asian dinners and toddler meals from a working mom in Vancouver.", "/recipes/")
      + header("/recipes/") + page_title("Recipes", "The South Asian dinners and toddler meals we actually make after work.")
      + f"""<section><div class="wrap">
    <div class="r-intro"><img src="/images/album/lunch.jpg" alt="Aanchal smiling at lunch" loading="lazy"><p>Food in our house is simple, quick and mostly South Asian. These are the dishes I lean on during a busy work week, plus a few my toddler actually eats. When we eat out, it's usually dosa.</p></div>
    {recipes_body}
    <div class="table-life">
      <h2 class="r-cat" style="margin-top:8px">Real life at our table</h2>
      <p class="tl-sub">Not every night is dal and roti. Here's how we actually eat, toddler and all.</p>
      <div class="tl-grid">
        <figure><img src="/images/album/eat-pizza.jpg" alt="Aanchal smiling with pizza and calzone" loading="lazy"><figcaption>Friday night pizza. Balance, right?</figcaption></figure>
        <figure><img src="/images/album/eat-coconut.jpg" alt="Aanchal with fresh coconuts" loading="lazy"><figcaption>Coconut water, always</figcaption></figure>
        <figure><img src="/images/album/cozy-sweater.jpg" alt="Aanchal smiling at brunch" loading="lazy"><figcaption>A slow weekend brunch</figcaption></figure>
      </div>
    </div>
</div></section>
""" + NEWS + footer())

# ================= BLOG =================
blog_body = ('<div class="b-grid">' + ''.join(f'<a class="b-card" href="/blog/{p["slug"]}/"><img src="{p.get("image","/images/aanchal-hero.jpg")}" alt="" loading="lazy"><h3>{html.escape(p["title"])}</h3><p>{html.escape(p["summary"])}</p></a>' for p in POSTS) + '</div>') if POSTS else """<div class="soon">
      <h3>First posts coming soon</h3>
      <p>Our mornings, how I fit workouts around a full-time job, and family life as it really goes.</p>
      <a class="btn" href="#newsletter">Get them by email</a>
    </div>"""
write("/blog/", head("Blog", "Working-mom routines, fitness and South Asian family life in Vancouver.", "/blog/")
      + header("/blog/") + page_title("Blog", "The parts of the week that don't fit in a Reel.")
      + f"""<section><div class="wrap">{blog_body}</div></section>
""" + NEWS + footer())

# ================= SHOP =================
if SHOP:
    favs = '<ul class="list-links">' + "\n".join(
        f'<li><strong><a href="{html.escape(p["url"])}" rel="sponsored noopener">{html.escape(p["name"])}</a></strong>{html.escape(p["why"])}</li>'
        for p in SHOP) + "</ul>"
else:
    favs = f"""<div class="partner"><div><h3>Avee Health</h3><p>A paid partnership: I made a UGC video for Avee Health, and they ran it as an ad.</p><p><a class="btn" href="{AVEE}" rel="noopener">Watch the video</a></p></div></div>"""
write("/shop/", head("Shop", "Aanchal's guides and the products she uses at home, at the gym and with her son.", "/shop/")
      + header("/shop/") + page_title("Shop", "My own guides, and the things I actually use.")
      + f"""<section style="padding:0"><div class="offers">
    <article><h3>The Working Mom's Weeknight Dinner Plan</h3><p class="meta">Free PDF guide, 12 pages</p><p>One week of South Asian dinners that fit around a full-time job and a toddler: the plan, a shopping list and 8 recipes.</p><p><a class="btn" href="/guides/weeknight-dinner-plan.pdf" download>Download free</a></p></article>
    <article><h3>Deals</h3><p class="meta">Member discounts</p><p>Discounts on Canadian brands for moms, toddlers and busy weeks.</p><p><a class="btn" href="/deals/">See deals</a></p></article>
    <article><h3>Recipes</h3><p class="meta">Free</p><p>Weeknight dinners and toddler meals from our kitchen.</p><p><a class="btn" href="/recipes/">See recipes</a></p></article>
  </div></section>
<section id="favourites"><div class="wrap">
    <h2 style="font-size:clamp(2rem,4vw,3rem);margin-bottom:24px">Brands I've worked with</h2>
    <p class="note">Paid partnerships are always labelled. <a href="/disclosure/">Read the full disclosure</a>.</p>
    {favs}
  </div></section>
""" + NEWS + footer())

# ================= DEALS =================
from deals import DEALS, GROUPS
def deal_card(d):
    name, grp, city, what, site, prog, deal = d
    badge = f'<span class="d-badge on">{html.escape(deal)}</span>' if deal else '<span class="d-badge">Deal coming</span>'
    return f'''<article class="deal"><div class="d-top">{badge}<span class="d-city">{html.escape(city)}</span></div>
      <h3>{html.escape(name)}</h3><p>{html.escape(what)}</p>
      <a class="btn btn-ghost-dark" href="{site}" rel="sponsored noopener" target="_blank">Shop {html.escape(name)}</a></article>'''
sections = "".join(
    f'<h2 class="d-group">{t}</h2><div class="deal-grid">' + "".join(deal_card(d) for d in DEALS if d[1] == g) + "</div>"
    for g, t in GROUPS if any(d[1] == g for d in DEALS))
write("/deals/", head("Deals for busy families", "Discounts on Canadian brands for moms, toddlers and busy families, curated by Aanchal Bathija.", "/deals/")
      + header("/deals/") + page_title("Deals", "Discounts on brands for moms, toddlers and busy weeks. Mostly Canadian, many local to BC.")
      + f"""<section><div class="wrap">
    <div class="d-unlock"><div><h2>Unlock member deals</h2><p>Codes for these brands go to my email list first. Join free and I'll send them as each one goes live.</p></div>
      <a class="btn" href="mailto:{EMAIL}?subject=Subscribe%20-%20deals&amp;body=Hi%20Aanchal%2C%20please%20send%20me%20your%20member%20deals.">Unlock deals by email</a></div>
    <p class="note">How this works: I earn a small commission when you buy through some of these links, at no extra cost to you. Paid partnerships are always labelled. <a href="/disclosure/">Full disclosure</a>.</p>
    {sections}
  </div></section>
""" + NEWS + footer())

# ================= WORK WITH ME =================
write("/work-with-me/", head("Work with me", "UGC videos, Reels and posts for brands that fit a busy family's week.", "/work-with-me/")
      + header("/work-with-me/") + page_title("Work with me", "UGC videos, Reels and posts, made from the real moments in my life where your product fits.")
      + f"""<section style="padding:0"><div class="offers">
    <article><h3>UGC video</h3><p class="meta">For your ads</p><p>An ad-ready video for your own ads, plus one bonus post on my page.</p></article>
    <article><h3>Video &amp; post</h3><p class="meta">Video + blog or recipe post</p><p>The video, plus a post on this site featuring your product, with the video embedded.</p></article>
    <article><h3>Video, post &amp; newsletter</h3><p class="meta">Full package</p><p>Everything in the video and post package, plus a mention in my monthly email.</p></article>
  </div></section>

<section class="olive"><div class="wrap">
    <h2 style="font-size:clamp(2rem,4vw,3rem);text-transform:uppercase;margin-bottom:40px">The numbers</h2>
    <dl class="stats">
      <div><dt>12M+</dt><dd>total views across 382 Instagram Reels</dd></div>
      <div><dt>3.6M</dt><dd>views on my most-watched Reel</dd></div>
      <div><dt>23</dt><dd>Reels with more than 100K views each</dd></div>
      <div><dt>4.2K</dt><dd>Instagram followers, growing with every viral Reel</dd></div>
    </dl>
    <p class="asof">Public counts as of November 2026.</p>
  </div></section>

<section><div class="wrap about-grid">
    <div>
      <h2 style="font-size:clamp(2rem,4vw,3rem);text-transform:uppercase;margin-bottom:20px">A good fit</h2>
      <p>Mom and baby, postpartum recovery, women's health and period care, activewear and fitness, healthy food, family travel, South Asian fashion and beauty, home organization for busy parents, and Vancouver and Canadian brands.</p>
      <p>I only share products I'd actually use, and I don't make health claims about any of them.</p>
      <p style="margin-top:28px"><a class="btn" href="mailto:{EMAIL}?subject=Collaboration">Email me</a></p>
      <p>Rates are shared by email.</p>
    </div>
    <div>
      <h3 style="font-size:1.4rem;font-weight:600;margin-bottom:10px">Recent work: Avee Health</h3>
      <p>A paid UGC video for Avee Health, a BC virtual-care service. They ran it as an ad.</p>
      {ig_embed(AVEE, "Watch the Avee Health video on Instagram")}
    </div>
  </div></section>
""" + footer(IG_SCRIPT))

# ================= CONTACT =================
write("/contact/", head("Contact", "Get in touch with Aanchal: brand collaborations, reader stories, recipes or just to say hi.", "/contact/")
      + header("/contact/") + page_title("Let's talk", "Brands, fellow moms, or just saying hi. I read every message.")
      + f"""<section><div class="wrap contact-grid">
    <div>
      <div class="c-options">
        <a class="c-opt" href="mailto:{EMAIL}?subject=Brand%20collaboration&body=Hi%20Aanchal%2C%0A%0ABrand%3A%20%0AProduct%3A%20%0AWhat%20we%20have%20in%20mind%3A%20%0ATimeline%2Fbudget%3A%20%0A%0AThanks!"><h3>Brand collaborations</h3><p>UGC videos, Reels, recipe or blog posts, newsletter mentions. Tell me about your product and timeline.</p><span>Email about a collab</span></a>
        <a class="c-opt" href="mailto:{EMAIL}?subject=My%20story%20for%20the%20blog"><h3>Share your story</h3><p>Replying to one of my blog posts? Send your take. With your permission, I may feature it (anonymously if you like).</p><span>Send your story</span></a>
        <a class="c-opt" href="mailto:{EMAIL}?subject=Recipe%20question"><h3>Recipes &amp; questions</h3><p>Tried a recipe, have a question, or want me to make something? I'd love to hear.</p><span>Ask me anything</span></a>
      </div>
      <p class="c-direct">Or email directly: <a href="mailto:{EMAIL}">{EMAIL}</a><br>I usually reply within 2–3 working days.</p>
      <div class="socials" style="margin-top:20px"><a href="{IG}" rel="noopener" style="border-color:var(--ink)">Instagram</a><a href="{YT}" rel="noopener" style="border-color:var(--ink)">YouTube</a><a href="{THREADS}" rel="noopener" style="border-color:var(--ink)">Threads</a></div>
    </div>
    <div>{photo("hero", "Aanchal Bathija")}<p class="c-loc">Based in Vancouver, BC. Working with brands across Canada and the US.</p></div>
  </div></section>
""" + footer())

# ================= DISCLOSURE =================
write("/disclosure/", head("Disclosure", "How Nurtured by Aanchal handles affiliate links and paid partnerships.", "/disclosure/")
      + header("/disclosure/") + page_title("Disclosure", "How I handle affiliate links, gifted products and paid partnerships.")
      + """<section><div class="wrap prose">
    <h2>Affiliate links</h2>
    <p>Some links on this site are affiliate links. If you click one and buy something, I may earn a small commission. It doesn't change the price you pay. Pages with affiliate links say so near the top.</p>
    <h2>Paid partnerships and gifted products</h2>
    <p>When a brand pays me or sends me a product, I say so clearly in that post or video. I only share products I've actually used, and my opinions are my own.</p>
    <h2>Not advice</h2>
    <p>I share what works for me and my family. Nothing on this site is medical, fitness or nutrition advice. Talk to your own doctor before changing your diet, exercise or treatment.</p>
  </div></section>
""" + footer())

# ================= PRIVACY =================
write("/privacy/", head("Privacy policy", "What Nurtured by Aanchal collects when you email, subscribe or browse the site, how it's used, and how to ask us to delete it.", "/privacy/")
      + header("/privacy/") + page_title("Privacy policy", "What this site collects, and what I do with it.")
      + f"""<section><div class="wrap prose">
    <p>Last updated: {date.today().strftime('%B %-d, %Y')}</p>
    <h2>What I collect</h2>
    <p>This site doesn't set cookies of its own. Embedded videos from YouTube and Instagram may set their own cookies under their own privacy policies.</p>
    <p>When the newsletter launches, you'll be able to sign up with your email address. I'll only email you once you confirm your sign-up, every email will have an unsubscribe link, and I'll never sell or share your address.</p>
    <p>If you email me, I keep your message so I can reply.</p>
    <h2>Questions or removal</h2>
    <p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> and I'll tell you what I hold about you or delete it.</p>
  </div></section>
""" + footer())

# ================= BLOG POST PAGES =================
def render_blocks(blocks):
    out = []
    for b in blocks:
        kind, val = b[0], b[1]
        if kind == "p":
            out.append(f"<p>{val}</p>")
        elif kind == "h":
            out.append(f"<h2>{html.escape(val)}</h2>")
        elif kind == "quote":
            out.append(f'<blockquote class="pull">{html.escape(val)}</blockquote>')
        elif kind == "yt":
            out.append(f'<div class="yt"><iframe src="https://www.youtube-nocookie.com/embed/{val}" title="{html.escape(b[2])}" loading="lazy" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe></div><p class="credit">{b[2]}</p>')
        elif kind == "img":
            out.append(f'<figure class="post-img"><img src="{val}" alt="{html.escape(b[2])}" loading="lazy"></figure>')
        elif kind == "ask":
            out.append(f'<div class="ask"><h3>{html.escape(val)}</h3><p>{b[2]}</p><p><a class="btn" href="{IG}" rel="noopener">Tell me on Instagram</a> <a class="btn btn-ghost-dark" href="mailto:{EMAIL}?subject={html.escape(val)}">Email me your take</a></p></div>')
    return "\n    ".join(out)

for p in POSTS:
    ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"],
          "description": p["summary"], "datePublished": p["date"],
          "author": {"@type": "Person", "name": "Aanchal Bathija"},
          "mainEntityOfPage": f'{SITE}/blog/{p["slug"]}/'}
    if p.get("image"):
        ld["image"] = [SITE + p["image"]]
    extra = f'<script type="application/ld+json">{json.dumps(ld)}</script>\n'
    write(f'/blog/{p["slug"]}/', head(p["title"], p["summary"], f'/blog/{p["slug"]}/', extra)
          + header("/blog/") + page_title(html.escape(p["title"]), html.escape(p["summary"])).replace('class="page-title"','class="page-title post-title"')
          + f"""<section><div class="wrap prose post">
    <p class="meta-line">By Aanchal Bathija · {html.escape(p["date_label"])} · {p.get("read","5 min read")}</p>
    {render_blocks(p["blocks"])}
  </div></section>
""" + NEWS + footer())

# ================= RECIPE PAGES (Google recipe rich results) =================
from recipe_extras import EXTRAS

def mins(n):
    return f"PT{n}M"

for r in RECIPES:
    ld = {"@context": "https://schema.org", "@type": "Recipe", "name": r["title"],
          "author": {"@type": "Person", "name": "Aanchal Bathija"}, "description": r["summary"],
          "recipeCuisine": "Indian", "prepTime": mins(r["prep"]), "cookTime": mins(r["cook"]),
          "totalTime": mins(r["prep"] + r["cook"]), "recipeYield": f'{r["servings"]} servings',
          "recipeIngredient": r["ingredients"],
          "recipeInstructions": [{"@type": "HowToStep", "text": s} for s in r["steps"]]}
    if r.get("image"):
        ld["image"] = [absurl(r["image"])]
    extra = f'<script type="application/ld+json">{json.dumps(ld)}</script>\n'
    ing = "".join(f"<li>{html.escape(i)}</li>" for i in r["ingredients"])
    steps = "".join(f"<li>{html.escape(s)}</li>" for s in r["steps"])
    story = "".join(f"<p>{html.escape(p)}</p>" for p in r.get("story", []))
    reel = ig_embed(r["reel"], "Watch the Reel") if r.get("reel") else ""
    aff = '<p class="note">This post has affiliate links. See the <a href="/disclosure/">disclosure</a>.</p>' if r.get("affiliate") else ""
    ing_count = len(r["ingredients"])
    x = EXTRAS.get(r["slug"], {})
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in x.get("faqs", [])]}
    if x.get("faqs"):
        extra += f'<script type="application/ld+json">{json.dumps(faq_ld)}</script>\n'
    subs = "".join(f"<tr><th>{html.escape(a)}</th><td>{html.escape(b)}</td></tr>" for a, b in x.get("subs", []))
    howto = "".join(f'<li><span class="hs-n">{i}</span><p>{html.escape(st)}</p></li>' for i, st in enumerate(r["steps"], 1))
    tips = "".join(f"<li>{html.escape(t)}</li>" for t in x.get("tips", []))
    faqs = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in x.get("faqs", []))
    related = "".join(
        f'<a class="r-card" href="/recipes/{o["slug"]}/"><img src="{o["image"]}" alt="{html.escape(o["title"])}" loading="lazy"><span class="r-meta">{o["prep"] + o["cook"]} min</span><h3>{html.escape(o["title"])}</h3></a>'
        for o in [o for o in RECIPES if o["slug"] != r["slug"] and o.get("cat") == r.get("cat")][:3] or [o for o in RECIPES if o["slug"] != r["slug"]][:3])
    toc = "".join(f'<li><a href="#{a}">{t}</a></li>' for a, t in [("about", "What is it"), ("ingredients", "Ingredients &amp; substitutes"), ("how", "How to make it"), ("tips", "Expert tips"), ("faqs", "FAQs"), ("recipe", "Recipe card")])
    write(f'/recipes/{r["slug"]}/', head(r["title"], r["summary"], f'/recipes/{r["slug"]}/', extra + f'<meta property="og:image" content="{absurl(r["image"])}">\n')
          + header("/recipes/") + page_title(html.escape(r["title"]), html.escape(r["summary"])).replace('class="page-title"','class="page-title post-title"')
          + f"""<section><div class="wrap prose post rp">
    <p class="meta-line">By Aanchal Bathija · {html.escape(r.get("cat",""))} · {r["prep"] + r["cook"]} min · serves {r["servings"]}</p>
    <p class="jump"><a class="btn" href="#recipe">Jump to recipe</a> <button class="btn btn-ghost-dark" onclick="window.print()">Print recipe</button></p>
    <figure class="post-img"><img src="{r["image"]}" alt="{html.escape(r["title"])}">{f'<figcaption class="credit">{r["credit"]}</figcaption>' if r.get("credit") else ""}</figure>
    {aff}
    <nav class="rp-toc" aria-label="On this page"><strong>On this page</strong><ul>{toc}</ul></nav>
    <h2 id="about">What is {html.escape(x.get("name", r["title"]))}?</h2><p>{html.escape(x.get("about",""))}</p>
    <h2>About my recipe</h2>{story}{reel}
    <h2 id="ingredients">Ingredients &amp; substitutes</h2>
    <p>You'll need {ing_count} ingredients, most of them pantry staples. The full amounts are in the <a href="#recipe">recipe card</a>. If you're missing something, here's what I swap in:</p>
    <table class="subs">{subs}</table>
    <h2 id="how">How to make it</h2>
    <ol class="howto">{howto}</ol>
    <h2 id="tips">Expert tips</h2><ul class="tips">{tips}</ul>
    <h2 id="faqs">FAQs</h2><div class="faqs">{faqs}</div>
    <aside class="from-a"><img src="/images/aanchal-kitchen.jpg" alt="Aanchal with her son"><div><strong>A note from me</strong><p>I cook for a full-time job, a toddler and a husband who's always hungry, so everything here is tested on real weeknights. Make it your own, and tell me how it went.</p></div></aside>
    <div class="recipe-card" id="recipe">
      <h2>{html.escape(r["title"])}</h2>
      <p class="rc-sum">{html.escape(r["summary"])}</p>
      <dl class="r-facts"><div><dt>Prep</dt><dd>{r["prep"]} min</dd></div><div><dt>Cook</dt><dd>{r["cook"]} min</dd></div><div><dt>Total</dt><dd>{r["prep"] + r["cook"]} min</dd></div><div><dt>Serves</dt><dd>{r["servings"]}</dd></div></dl>
      <h3>Ingredients</h3><ul class="ing">{ing}</ul>
      <h3>Method</h3><ol class="method">{steps}</ol>
      <p class="r-note">Made this? Tag <a href="{IG}" rel="noopener">@nurturedbyaanchal</a> on Instagram, I'd love to see it.</p>
      <button class="btn btn-ghost-dark print-btn" onclick="window.print()">Print recipe</button>
    </div>
    <h2>More recipes you'll like</h2>
  </div><div class="wrap"><div class="r-grid">{related}</div></div></section>
""" + NEWS + footer(IG_SCRIPT))

# ================= SITEMAP =================
paths = ["/", "/deals/", "/about/", "/recipes/", "/blog/", "/shop/", "/work-with-me/", "/contact/", "/disclosure/", "/privacy/"]
paths += [f"/recipes/{r['slug']}/" for r in RECIPES] + [f"/blog/{p['slug']}/" for p in POSTS]
with open("sitemap.xml", "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for p in paths:
        f.write(f"  <url><loc>{SITE}{p}</loc></url>\n")
    f.write("</urlset>\n")
print("built", len(paths), "pages")
