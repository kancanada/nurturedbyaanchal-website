"""Builds the Nurtured by Aanchal static site.

Run from the repo root:  python3 _tools/build.py
Content (recipes, posts, shop picks) lives in _tools/content.py.
Photos: drop them in /images with the names in PHOTOS below and rebuild; until then a placeholder shows.
"""
import json, os, html
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

NAV = [("Home", "/"), ("About", "/about/"), ("Recipes", "/recipes/"), ("Shop", "/shop/"), ("Contact", "/contact/")]

try:
    from content import RECIPES, POSTS, SHOP
except ImportError:
    RECIPES, POSTS, SHOP = [], [], []


def photo(key, alt):
    p = PHOTOS[key]
    if os.path.exists(p):
        return f'<div class="photo"><img src="/{p}" alt="{html.escape(alt)}"></div>'
    return '<div class="photo empty" role="img" aria-label="Photo of Aanchal"><span>AB</span></div>'


def head(title, desc, path, extra=""):
    full = title if path == "/" else f"{title} | Nurtured by Aanchal"
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
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
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
    <nav class="site-nav" aria-label="Main">
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
    <p>(The newsletter is starting soon. Follow along on Instagram until then.)</p>
    <a class="btn" href="{IG}" rel="noopener">Follow on Instagram</a>
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


def write(path, body):
    out = path.strip("/")
    if out:
        os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "index.html") if out else "index.html", "w") as f:
        f.write(body)


def page_title(h1, p):
    return f"""<div class="page-title"><div class="wrap"><h1>{h1}</h1><p>{p}</p></div></div>\n"""


IG_SCRIPT = '<script async src="https://www.instagram.com/embed.js"></script>\n'


def ig_embed(url, label):
    return (f'<div class="ig-wrap"><blockquote class="instagram-media" data-instgrm-permalink="{url}" data-instgrm-version="14">'
            f'<a href="{url}" style="display:block;padding:20px">{label}</a></blockquote></div>')


def link_list(items, base):
    return '<ul class="list-links">' + "\n".join(
        f'<li><strong><a href="{base}{i["slug"]}/">{html.escape(i["title"])}</a></strong>{html.escape(i["summary"])}</li>'
        for i in items) + "</ul>"


# ================= HOME =================
home = head("Nurtured by Aanchal | Real mom life in Vancouver",
            "Aanchal Bathija is a working mom in Vancouver sharing postpartum fitness, family life, toddler meals and the routines that get her through the week.",
            "/") + header("/") + f"""
<section class="hero" style="padding-top:20px">
  <div class="wrap">
    <h1 class="hero-name">Aanchal Bathija</h1>
    <div class="hero-grid">
      <div class="hero-left">
        <p class="hero-sub">Nurtured by Aanchal</p>
        <p><span class="mark-hl">Working mom, toddler mom and wife, figuring out how to look after everyone, including myself.</span></p>
        <p class="hero-pillars">Mom life. Fitness. Family. Real routines.</p>
        <p><a class="btn" href="{IG}" rel="noopener">Follow my journey</a></p>
      </div>
      <div class="hero-photo">
        {photo("hero", "Aanchal Bathija")}
      </div>
    </div>
  </div>
</section>

<section class="statement">
  <div class="wrap">
    <h2>Helping new moms make time for themselves, honestly, between a full-time job, a toddler and family life.</h2>
  </div>
</section>

<section class="olive center">
  <div class="wrap">
    <div class="pairs">
      <h3>Feeling guilty for taking an hour at the gym?</h3>
      <h3 class="answer">Not anymore.</h3>
      <h3>Mom content that looks nothing like real life?</h3>
      <h3 class="answer">Not here.</h3>
      <h3>Choosing between your career, your family and yourself?</h3>
      <h3 class="answer">Why not all three.</h3>
    </div>
    <a class="btn btn-light" href="{IG}" rel="noopener">Follow along</a>
  </div>
</section>

<section>
  <div class="wrap about-grid">
    {photo("about", "Aanchal with her son")}
    <div>
      <p class="lead">Becoming a mom changed everything, including how much of me was left at the end of the day.</p>
      <p>I work full time in home insurance. My husband Anuj and I are raising our two-year-old son in Vancouver, in a home full of South Asian food, family and culture.</p>
      <p>Somewhere in the middle of all that, I decided my health and my time mattered too. So I started training again, and I started sharing it, the good days and the messy ones.</p>
      <p>Now I share what actually works for us: workouts that fit around a workday, family meals, marriage, and the conversations South Asian families don't always have out loud.</p>
      <h2 class="hi">Hi, I'm Aanchal.</h2>
      <p class="creds">Working mom. Content creator. Vancouver.</p>
      <a class="btn" href="/about/">My story</a>
    </div>
  </div>
</section>

<section class="feature">
  <div class="wrap">
    <h3>Recent work: a paid UGC video for Avee Health, a BC virtual-care service.</h3>
    <p>I made it from a real moment in our life: getting a doctor for my son from home instead of waiting hours in the ER. Avee Health liked it enough to run it as an ad.</p>
    <p class="who"><a href="{AVEE}" rel="noopener">Watch the video on Instagram</a></p>
  </div>
</section>


<section class="gallery-sec">
  <div class="wrap">
    <h2 class="gal-title">Life lately</h2>
    <p class="gal-sub">From the bump to the toddler years, and every trip in between.</p>
    <div class="gallery">
      <figure class="g-tall"><img src="/images/album/seattle-lift.webp" alt="Aanchal lifting her baby son into the air on the Seattle waterfront" loading="lazy"><figcaption>Seattle waterfront</figcaption></figure>
      <figure><img src="/images/album/pregnant-market.jpg" alt="Aanchal pregnant at a flower market" loading="lazy"><figcaption>Waiting for him</figcaption></figure>
      <figure><img src="/images/album/newborn-forest.jpg" alt="Aanchal holding her newborn son in a forest" loading="lazy"><figcaption>First walks</figcaption></figure>
      <figure><img src="/images/album/family-beach.jpg" alt="Aanchal, Anuj and their son at the beach" loading="lazy"><figcaption>Family beach days</figcaption></figure>
      <figure><img src="/images/album/statue-of-liberty.jpg" alt="Aanchal with the Statue of Liberty behind her" loading="lazy"><figcaption>New York</figcaption></figure>
      <figure><img src="/images/album/swing.jpg" alt="Aanchal and her son on a swing" loading="lazy"><figcaption>Park afternoons</figcaption></figure>
      <figure><img src="/images/album/brooklyn-bridge.jpg" alt="Aanchal on the Brooklyn Bridge" loading="lazy"><figcaption>Brooklyn Bridge</figcaption></figure>
      <figure><img src="/images/album/sunglasses-son.jpg" alt="Aanchal and her son in matching sunglasses" loading="lazy"><figcaption>Matching shades</figcaption></figure>
      <figure><img src="/images/album/couple-mountains.jpg" alt="Aanchal and Anuj in the mountains" loading="lazy"><figcaption>Us two</figcaption></figure>
    </div>
    <p style="text-align:center;margin-top:40px"><a class="btn" href="{IG}" rel="noopener">See more on Instagram</a></p>
  </div>
</section>

<section class="olive share">
  <div class="wrap">
    <h2>What I talk about</h2>
    <ul>
      <li>Postpartum &amp; mom fitness</li>
      <li>Working-mom routines</li>
      <li>Women's health</li>
      <li>Marriage &amp; relationships</li>
      <li>South Asian family life</li>
      <li>Toddler meals</li>
      <li>Family travel</li>
      <li>Mindset &amp; motivation</li>
      <li>Honest product reviews</li>
    </ul>
  </div>
</section>

<div class="marquee" aria-label="Vancouver-based working mom">
  <div class="marquee-track" aria-hidden="true">
    <span>Vancouver-based 〰️ Working mom 〰️ Vancouver-based 〰️ Working mom 〰️</span>
    <span>Vancouver-based 〰️ Working mom 〰️ Vancouver-based 〰️ Working mom 〰️</span>
  </div>
</div>

<section class="lists">
  <div class="wrap">
    <div class="card">
      <p class="label">You're juggling…</p>
      <ul>
        <li>A full-time job and a little one who needs you the minute you get home</li>
        <li>Dinner, daycare pickups, laundry and bedtime, every single day</li>
        <li>A body that changed after baby and a routine that disappeared</li>
        <li>Family expectations, and the "log kya kahenge" voice in your head</li>
        <li>A marriage that needs time too</li>
      </ul>
    </div>
    <div class="card">
      <p class="label">You feel like…</p>
      <ul>
        <li>There's no time left for you</li>
        <li>Every other mom has it figured out</li>
        <li>Taking an hour for yourself is selfish</li>
        <li>You've lost a bit of who you were before baby</li>
        <li>You're doing it all, and nobody sees it</li>
      </ul>
    </div>
  </div>
</section>

<section class="big">
  <div class="wrap">
    <h2>Enough of "You're so lucky you have time to work out."</h2>
    <h2>Let's talk about how it actually happens.</h2>
  </div>
</section>

<section class="olive">
  <div class="wrap split-photo">
    <div>
      <h2>every mom's week looks different.</h2>
      <p class="bold">Mine has a full-time job, a toddler and a workout squeezed in somewhere.</p>
      <p>I don't have a perfect routine, and I don't pretend to. What I share is the real version: what we eat on a Tuesday, how I fit training around work, how Anuj and I make it work, and what I'm still figuring out.</p>
      <p>If you're a new mom trying to make room for yourself, you'll find something here that helps.</p>
      <p><a class="btn btn-light" href="/blog/">Read the blog</a></p>
    </div>
    {photo("family", "Aanchal with her family")}
  </div>
</section>

<section style="padding:0">
  <div class="offers">
    <article>
      <h3><a href="/recipes/">Recipes</a></h3>
      <p class="meta">Weeknight meals</p>
      <p>The South Asian dinners and toddler meals we actually make after work.</p>
    </article>
    <article>
      <h3><a href="/shop/">Shop</a></h3>
      <p class="meta">Guides &amp; my favourites</p>
      <p>My own guides, plus the things I use at home, at the gym and with my son.</p>
    </article>
    <article>
      <h3><a href="/work-with-me/">Brands</a></h3>
      <p class="meta">UGC videos, Reels &amp; posts</p>
      <p>Content made from the real moments in my life where your product fits.</p>
    </article>
  </div>
</section>

<section class="fit">
  <div class="wrap">
    <h2>Want to work together?</h2>
    <p>I make UGC videos brands can run as ads, plus Reels, stories and posts on my own page.</p>
    <p>Have a product that fits a busy family's week? I'd love to hear about it.</p>
    <a class="btn" href="/work-with-me/">Work with me</a>
  </div>
</section>

<section class="watch olive">
  <div class="wrap">
    <h2>Real moments from real life</h2>
    <div class="watch-grid">
      <figure>
        <iframe src="https://www.youtube-nocookie.com/embed/{SHORT}" title="Are Indian parents toxic, or is it unintentional emotional guilt?" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        <figcaption>"Are Indian parents toxic, or is it unintentional emotional guilt?" 60K views</figcaption>
      </figure>
      <figure>
        {ig_embed(AVEE, "Watch the Avee Health video on Instagram")}
        <figcaption>Paid UGC video for Avee Health, run as an ad</figcaption>
      </figure>
    </div>
  </div>
</section>

{NEWS}""" + footer(IG_SCRIPT)
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
recipes_body = link_list(RECIPES, "/recipes/") if RECIPES else """<div class="soon">
      <h3>The first recipes are on their way</h3>
      <p>Each one will have prep and cook times, ingredients, steps and the Reel where I make it.</p>
      <a class="btn" href="#newsletter">Get them by email</a>
    </div>"""
write("/recipes/", head("Recipes", "Weeknight South Asian dinners and toddler meals from a working mom in Vancouver.", "/recipes/")
      + header("/recipes/") + page_title("Recipes", "The South Asian dinners and toddler meals we actually make after work.")
      + f"""<section><div class="wrap">{recipes_body}</div></section>
""" + NEWS + footer())

# ================= BLOG =================
blog_body = link_list(POSTS, "/blog/") if POSTS else """<div class="soon">
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
    favs = """<div class="soon"><h3>My picks are coming soon</h3><p>I'm only adding things I actually use at home, at the gym and with my son.</p></div>"""
write("/shop/", head("Shop", "Aanchal's guides and the products she uses at home, at the gym and with her son.", "/shop/")
      + header("/shop/") + page_title("Shop", "My own guides, and the things I actually use.")
      + f"""<section style="padding:0"><div class="offers">
    <article><h3>E-books &amp; guides</h3><p class="meta">Coming soon</p><p>My first guide for busy moms is in the works. Join the list to hear first.</p><p><a class="btn" href="#newsletter">Get notified</a></p></article>
    <article><h3>My favourites</h3><p class="meta">Home, gym &amp; toddler</p><p>The products we use every week, in one place.</p><p><a class="btn" href="#favourites">See my picks</a></p></article>
    <article><h3>Recipes</h3><p class="meta">Free</p><p>Weeknight dinners and toddler meals from our kitchen.</p><p><a class="btn" href="/recipes/">See recipes</a></p></article>
  </div></section>
<section id="favourites"><div class="wrap">
    <h2 style="font-size:clamp(2rem,4vw,3rem);text-transform:uppercase;margin-bottom:24px">My favourites</h2>
    <p class="note">Some links on this page are affiliate links. If you buy through them, I may earn a small commission at no extra cost to you. I only list products I use. <a href="/disclosure/">Read the full disclosure</a>.</p>
    {favs}
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
      <div><dt>4.1K</dt><dd>Instagram followers</dd></div>
      <div><dt>61.8K</dt><dd>views on "Is marriage really patriarchal?"</dd></div>
      <div><dt>60K</dt><dd>views on my most-watched YouTube Short</dd></div>
      <div><dt>580+</dt><dd>posts on Instagram</dd></div>
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
write("/contact/", head("Contact", "Get in touch with Aanchal about collaborations, recipes or just to say hi.", "/contact/")
      + header("/contact/") + page_title("Contact", "Brands, fellow moms, or just saying hi: email is the best way to reach me.")
      + f"""<section><div class="wrap prose">
    <p style="font-size:clamp(1.3rem,3vw,2rem);font-weight:600"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <p>For collaborations, tell me a little about your brand and what you have in mind. You can also see <a href="/work-with-me/">how I work with brands</a>.</p>
    <p>Or find me on <a href="{IG}" rel="noopener">Instagram</a>, <a href="{YT}" rel="noopener">YouTube</a> and <a href="{THREADS}" rel="noopener">Threads</a>.</p>
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
write("/privacy/", head("Privacy policy", "What Nurtured by Aanchal collects and how it's used.", "/privacy/")
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

# ================= RECIPE PAGES (Google recipe rich results) =================
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
        ld["image"] = [SITE + r["image"]]
    extra = f'<script type="application/ld+json">{json.dumps(ld)}</script>\n'
    ing = "".join(f"<li>{html.escape(i)}</li>" for i in r["ingredients"])
    steps = "".join(f"<li>{html.escape(s)}</li>" for s in r["steps"])
    story = "".join(f"<p>{html.escape(p)}</p>" for p in r.get("story", []))
    reel = ig_embed(r["reel"], "Watch the Reel") if r.get("reel") else ""
    aff = '<p class="note">This post has affiliate links. See the <a href="/disclosure/">disclosure</a>.</p>' if r.get("affiliate") else ""
    write(f'/recipes/{r["slug"]}/', head(r["title"], r["summary"], f'/recipes/{r["slug"]}/', extra)
          + header("/recipes/") + page_title(html.escape(r["title"]), html.escape(r["summary"]))
          + f"""<section><div class="wrap prose">{aff}{story}{reel}
    <h2>Ingredients</h2><p>Prep {r["prep"]} min · Cook {r["cook"]} min · Serves {r["servings"]}</p><ul>{ing}</ul>
    <h2>Steps</h2><ol>{steps}</ol>
  </div></section>
""" + NEWS + footer(IG_SCRIPT))

# ================= SITEMAP =================
paths = ["/", "/about/", "/recipes/", "/blog/", "/shop/", "/work-with-me/", "/contact/", "/disclosure/", "/privacy/"]
paths += [f"/recipes/{r['slug']}/" for r in RECIPES] + [f"/blog/{p['slug']}/" for p in POSTS]
with open("sitemap.xml", "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for p in paths:
        f.write(f"  <url><loc>{SITE}{p}</loc></url>\n")
    f.write("</urlset>\n")
print("built", len(paths), "pages")
