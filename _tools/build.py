"""Builds the Nurtured by Aanchal static site.

Run from the repo root:  python3 _tools/build.py
Each page below is written to <slug>/index.html with the shared header and footer.
Recipes and blog posts are added in _tools/content.py (see RECIPES / POSTS).
"""
import json, os, html
from datetime import date

SITE = "https://nurturedbyaanchal.com"
EMAIL = "nurturedbyaanchal@gmail.com"
IG = "https://www.instagram.com/nurturedbyaanchal/"
YT = "https://www.youtube.com/@NurturedByAanchal"
THREADS = "https://www.threads.net/@nurturedbyaanchal"
AVEE = "https://www.instagram.com/reel/DahF_vBMJ8L/"

NAV = [("Recipes", "/recipes/"), ("Blog", "/blog/"), ("Shop", "/shop/"),
       ("About", "/about/"), ("Work with me", "/work-with-me/")]

try:
    from content import RECIPES, POSTS, SHOP
except ImportError:
    RECIPES, POSTS, SHOP = [], [], []


def head(title, desc, path, extra=""):
    full = f"{title} | Nurtured by Aanchal" if path != "/" else title
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
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,500;12..96,700;12..96,800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
{extra}</head>
<body>
"""


def header(path, inner):
    links = "\n".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if path.startswith(h) else ""}>{t}</a></li>'
        for t, h in NAV)
    return f"""<header>
  <div class="wrap">
    <div class="bar">
      <a class="mark" href="/">Nurtured by <span>Aanchal</span></a>
      <nav aria-label="Main"><ul>
{links}
      </ul></nav>
    </div>
{inner}
  </div>
</header>
<main>
"""


def page_head(h1, p):
    return f"""    <div class="page-head">
      <h1>{h1}</h1>
      <p>{p}</p>
    </div>"""


SIGNUP = f"""<section class="signup" id="newsletter">
  <div class="wrap">
    <h2>Get the weeknight list</h2>
    <p>A monthly email with my PCOS-friendly dinners, toddler lunchbox ideas and whatever's working in our routine. The newsletter is starting soon. Until then, the recipes go up on Instagram first.</p>
    <a class="btn btn-primary" href="{IG}" rel="noopener">Follow on Instagram</a>
  </div>
</section>
"""


def footer(scripts=""):
    return f"""</main>
<footer>
  <div class="wrap">
    <span>Nurtured by Aanchal, Vancouver, BC · <a href="mailto:{EMAIL}">{EMAIL}</a></span>
    <span class="footlinks">
      <a href="{IG}" rel="noopener">Instagram</a>
      <a href="{YT}" rel="noopener">YouTube</a>
      <a href="/disclosure/">Disclosure</a>
      <a href="/privacy/">Privacy</a>
      <span>© {date.today().year} Aanchal Bathija</span>
    </span>
  </div>
</footer>
{scripts}</body>
</html>
"""


def write(path, body):
    out = path.strip("/")
    os.makedirs(out or ".", exist_ok=True)
    with open(os.path.join(out, "index.html") if out else "index.html", "w") as f:
        f.write(body)


# ---------- Home ----------
def card_list(items, base):
    if not items:
        return None
    lis = "\n".join(
        f'<li><strong><a href="{base}{i["slug"]}/">{html.escape(i["title"])}</a></strong>'
        f'<span>{html.escape(i["summary"])}</span></li>' for i in items[:6])
    return f'<ul class="topics">\n{lis}\n</ul>'


home_hero = f"""    <div class="hero">
      <div>
        <h1>
          <span class="line">Full-time job.</span>
          <span class="line">Two-year-old.</span>
          <span class="line">Still cooking dal.</span>
        </h1>
        <p>I'm Aanchal, a working mom in Vancouver with PCOS. I share PCOS-friendly South Asian meals, toddler lunchboxes and the routines that get our family through the week.</p>
        <div class="actions">
          <a class="btn btn-primary" href="/recipes/">See the recipes</a>
          <a class="btn btn-ghost" href="/about/">About me</a>
        </div>
      </div>
      <div class="phone-col">
        <div class="phone">
          <iframe src="https://www.youtube-nocookie.com/embed/1Y15WDU7Q_k" title="YouTube Short: Are Indian parents toxic, or is it unintentional emotional guilt?" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
        <p class="phone-cap">"Are Indian parents toxic, or is it unintentional emotional guilt?" 60K views on YouTube.</p>
      </div>
    </div>"""

latest = card_list(RECIPES, "/recipes/") or """<div class="empty">
        <h3>The first recipes are on their way</h3>
        <p>I'm writing up the dinners I make most often on weeknights, with times, ingredients and the Reel for each.</p>
        <a class="btn btn-primary" href="#newsletter">Get them by email</a>
      </div>"""

home = head("Nurtured by Aanchal: PCOS-friendly South Asian meals for busy moms",
            "PCOS-friendly South Asian recipes, toddler lunchboxes and real routines from Aanchal, a working mom in Vancouver.",
            "/") + header("/", home_hero) + f"""
<section class="familiar">
  <div class="wrap">
    <h2>Sound familiar?</h2>
    <ul class="statements">
      <li><strong>Home at six, hungry toddler, no plan.</strong><span>Dinners I can make in about 30 minutes, with the dal, sabzi and rotis we already eat.</span></li>
      <li><strong>"Healthy" recipes that don't taste like home.</strong><span>The South Asian food I grew up with, made in a way that works for me with PCOS.</span></li>
      <li><strong>No time for yourself, let alone the gym.</strong><span>The routines that let me fit workouts around a full-time job and a two-year-old.</span></li>
    </ul>
  </div>
</section>

<section class="intro">
  <div class="wrap split">
    <div class="portrait" role="img" aria-label="Photo of Aanchal coming soon"><span>A</span></div>
    <div>
      <h2>Hi, I'm Aanchal.</h2>
      <p class="lede">I work full time in home insurance, I'm raising a two-year-old with my husband Anuj, and I have PCOS. Most nights the question is the same: how do I get a good dinner on the table without it taking all evening? This is where I share what works for us.</p>
      <a class="btn btn-primary" href="/about/">My story</a>
    </div>
  </div>
</section>

<div class="strip" aria-hidden="true"><span>Weeknight South Asian meals · Toddler lunchboxes · Working-mom routines · From a Vancouver kitchen</span></div>

<section id="latest">
  <div class="wrap">
    <h2>Latest recipes</h2>
    <p class="lede">Quick weeknight dal, sabzi, rotis and tiffin ideas, made the way I make them after work.</p>
    {latest}
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Shop</h2>
    <p class="lede">My own meal plans, and the things I actually use at home.</p>
    <ul class="packages two">
      <li class="feature"><h3>PCOS-friendly weeknight meal plan</h3><p>My go-to South Asian dinners for a busy work week, in one guide. Coming soon.</p><p class="cardlink"><a href="#newsletter">Hear when it's out</a></p></li>
      <li><h3>Shop my favourites</h3><p>Kitchen, gym and toddler things from our home, in one place.</p><p class="cardlink"><a href="/shop/#favourites">See my picks</a></p></li>
    </ul>
  </div>
</section>

{SIGNUP}
<section>
  <div class="wrap split">
    <div>
      <h2>For brands</h2>
      <p class="lede">I make UGC videos brands run as ads, plus Reels, recipe posts and stories on my own page.</p>
      <a class="btn btn-primary" href="/work-with-me/">Work with me</a>
    </div>
    <div>
      <h2>Say hello</h2>
      <p class="lede">Questions about a recipe or a collaboration? Email me at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </div>
  </div>
</section>
""" + footer()
write("/", home)

# ---------- Recipes ----------
recipes_body = card_list(RECIPES, "/recipes/") or """<div class="empty">
      <h3>The first recipes are on their way</h3>
      <p>Each one will have prep and cook times, ingredients, steps and the Reel where I make it.</p>
      <a class="btn btn-primary" href="#newsletter">Get them by email</a>
    </div>"""
write("/recipes/", head("Recipes", "PCOS-friendly South Asian recipes and toddler lunchboxes for busy weeknights.", "/recipes/")
      + header("/recipes/", page_head("Recipes", "PCOS-friendly South Asian dinners, toddler lunchboxes and snacks that fit a weeknight after work."))
      + f"""<section><div class="wrap">
    <p class="note">I have PCOS and these are the meals that work for me. They're not medical advice, so check with your own doctor or dietitian about what's right for you.</p>
    {recipes_body}
  </div></section>
""" + SIGNUP + footer())

# ---------- Blog ----------
blog_body = card_list(POSTS, "/blog/") or """<div class="empty">
      <h3>First posts coming soon</h3>
      <p>Our mornings, how I fit workouts around a full-time job, and family life as it really goes.</p>
      <a class="btn btn-primary" href="#newsletter">Get them by email</a>
    </div>"""
write("/blog/", head("Blog", "Working-mom routines, life with PCOS and South Asian family life in Vancouver.", "/blog/")
      + header("/blog/", page_head("Blog", "Mornings, workouts, bedtime, PCOS life and family. The parts of the week that don't fit in a Reel."))
      + f"""<section><div class="wrap">{blog_body}</div></section>
""" + SIGNUP + footer())

# ---------- Shop ----------
if SHOP:
    shop_list = '<ul class="topics">' + "\n".join(
        f'<li><strong><a href="{html.escape(p["url"])}" rel="sponsored noopener">{html.escape(p["name"])}</a></strong>'
        f'<span>{html.escape(p["why"])}</span></li>' for p in SHOP) + "</ul>"
else:
    shop_list = """<div class="empty">
      <h3>My picks are coming soon</h3>
      <p>I'm only adding things I actually use at home, in the kitchen, at the gym and with my son.</p>
    </div>"""
write("/shop/", head("Shop my favourites", "Products Aanchal uses at home, in the kitchen and at the gym.", "/shop/")
      + header("/shop/", page_head("Shop my favourites", "Things I actually use: in the kitchen, at the gym and with a toddler."))
      + f"""<section><div class="wrap">
    <h2>Guides and meal plans</h2>
    <p class="lede">My PCOS-friendly weeknight meal plan is in the works: the South Asian dinners I rely on during a busy week, in one guide.</p>
    <div class="empty" style="margin-bottom:24px"><h3>Coming soon</h3><p>Join the list and you'll hear first.</p><a class="btn btn-primary" href="#newsletter">Get notified</a></div>
  </div></section>
<section id="favourites" class="numbers"><div class="wrap">
    <h2>My favourites</h2>
    <p class="note">Some links on this page are affiliate links. If you buy through them, I may earn a small commission at no extra cost to you. I only list products I use. <a href="/disclosure/">Read the full disclosure</a>.</p>
    {shop_list}
  </div></section>
""" + footer())

# ---------- About ----------
write("/about/", head("About Aanchal", "Aanchal Bathija is a working mom in Vancouver sharing PCOS-friendly South Asian meals and real family routines.", "/about/")
      + header("/about/", page_head("Hi, I'm Aanchal", "A working mom in Vancouver, cooking for a family of three and trying to look after myself too."))
      + f"""<section><div class="wrap prose">
    <p>I work full time in home insurance. My husband Anuj and I have a two-year-old son, and most of our evenings are about getting a good dinner on the table without it taking all night.</p>
    <p>I also have PCOS. I'm not a doctor or a nutritionist, so I don't tell anyone what to eat. I share the South Asian meals and routines that work for me and my family, and I'm honest about what doesn't.</p>
    <p>Nurtured by Aanchal started on Instagram, where I talk about postpartum fitness, women's health, marriage and family, and South Asian life in Canada. This site is where the recipes and routines live in full.</p>
    <h2>Find me</h2>
    <p><a href="{IG}" rel="noopener">Instagram @nurturedbyaanchal</a> · <a href="{YT}" rel="noopener">YouTube</a> · <a href="{THREADS}" rel="noopener">Threads</a></p>
    <p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </div></section>
""" + SIGNUP + footer())

# ---------- Work with me ----------
write("/work-with-me/", head("Work with me", "UGC videos, Reels and recipe posts for brands that fit busy South Asian moms in Canada.", "/work-with-me/")
      + header("/work-with-me/", page_head("Work with me", "UGC videos, Reels and recipe posts for brands that fit a busy family's real week."))
      + f"""<section><div class="wrap">
    <h2>Packages</h2>
    <p class="lede">Every package is built around a real moment in my week where your product fits. Rates are shared by email.</p>
    <ul class="packages">
      <li><h3>UGC video</h3><p>An ad-ready video for your own ads, plus one bonus post on my page.</p></li>
      <li class="feature"><h3>Video and recipe post</h3><p>The video, plus a recipe or routine post on this site featuring your product, with the video embedded.</p></li>
      <li><h3>Video, post and newsletter</h3><p>Everything in the video and post package, plus a mention in my monthly email.</p></li>
    </ul>
  </div></section>

<section class="numbers">
  <div class="wrap">
    <h2>The numbers</h2>
    <p class="lede">Small, real and growing. These are public counts, not estimates.</p>
    <dl class="stats">
      <div><dt>4.1K</dt><dd>Instagram followers</dd></div>
      <div><dt>61.8K</dt><dd>views on "Is marriage really patriarchal?"</dd></div>
      <div><dt>60K</dt><dd>views on my most-watched YouTube Short</dd></div>
      <div><dt>580+</dt><dd>posts on Instagram</dd></div>
    </dl>
    <p class="asof">As of November 2026.</p>
  </div>
</section>

<section>
  <div class="wrap work-grid">
    <div>
      <h2>A good fit</h2>
      <p class="lede">Mom and baby, postpartum recovery, women's health and period care, activewear and fitness, healthy food and kitchen, family travel, South Asian fashion and beauty, home organization for busy parents, and Vancouver and Canadian brands.</p>
      <p class="fit">I don't make medical or health claims about any product, and I only share things I'd actually use.</p>
      <p><a class="btn btn-primary" href="mailto:{EMAIL}?subject=Collaboration">Email me about a collaboration</a></p>
    </div>
    <aside class="proof" aria-labelledby="proof-h">
      <h3 id="proof-h">Recent work: Avee Health</h3>
      <p>A paid UGC video for Avee Health, a BC virtual-care service. They ran it as an ad.</p>
      <div class="embed">
        <blockquote class="instagram-media" data-instgrm-permalink="{AVEE}" data-instgrm-version="14">
          <a class="fallback" href="{AVEE}" style="display:block;padding:20px;color:#2E1A2B">Watch the Avee Health video on Instagram</a>
        </blockquote>
      </div>
    </aside>
  </div>
</section>
""" + footer('<script async src="https://www.instagram.com/embed.js"></script>\n'))

# ---------- Disclosure ----------
write("/disclosure/", head("Disclosure", "How Nurtured by Aanchal handles affiliate links and paid partnerships.", "/disclosure/")
      + header("/disclosure/", page_head("Disclosure", "How I handle affiliate links, gifted products and paid partnerships."))
      + """<section><div class="wrap prose">
    <h2>Affiliate links</h2>
    <p>Some links on this site are affiliate links. If you click one and buy something, I may earn a small commission. It doesn't change the price you pay. Pages with affiliate links say so near the top.</p>
    <h2>Paid partnerships and gifted products</h2>
    <p>When a brand pays me or sends me a product, I say so clearly in that post or video. I only share products I've actually used, and my opinions are my own.</p>
    <h2>Health</h2>
    <p>I have PCOS and share what works for me. Nothing on this site is medical advice. Please talk to your own doctor or dietitian before changing your diet, exercise or treatment.</p>
  </div></section>
""" + footer())

# ---------- Privacy ----------
write("/privacy/", head("Privacy policy", "What Nurtured by Aanchal collects and how it's used.", "/privacy/")
      + header("/privacy/", page_head("Privacy policy", "What this site collects, and what I do with it."))
      + f"""<section><div class="wrap prose">
    <p>Last updated: {date.today().strftime('%B %-d, %Y')}</p>
    <h2>What I collect</h2>
    <p>This site doesn't use cookies of its own. Embedded videos from YouTube and Instagram may set their own cookies under their own privacy policies.</p>
    <p>When the newsletter launches, you'll be able to sign up with your email address. I'll only email you if you confirm your sign-up, every email will have an unsubscribe link, and I'll never sell or share your address.</p>
    <p>If you email me, I keep your message so I can reply.</p>
    <h2>Questions or removal</h2>
    <p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> and I'll tell you what I hold about you or delete it.</p>
  </div></section>
""" + footer())

# ---------- Recipe pages (Google recipe rich results) ----------
def mins(n):
    return f"PT{n}M"

for r in RECIPES:
    ld = {"@context": "https://schema.org", "@type": "Recipe", "name": r["title"],
          "author": {"@type": "Person", "name": "Aanchal Bathija"},
          "description": r["summary"], "recipeCuisine": "Indian",
          "prepTime": mins(r["prep"]), "cookTime": mins(r["cook"]),
          "totalTime": mins(r["prep"] + r["cook"]), "recipeYield": f'{r["servings"]} servings',
          "recipeIngredient": r["ingredients"],
          "recipeInstructions": [{"@type": "HowToStep", "text": s} for s in r["steps"]]}
    if r.get("image"):
        ld["image"] = [SITE + r["image"]]
    if r.get("reel"):
        ld["video"] = {"@type": "VideoObject", "name": r["title"], "description": r["summary"],
                       "contentUrl": r["reel"], "uploadDate": r.get("date", str(date.today())),
                       "thumbnailUrl": [SITE + r["image"]] if r.get("image") else []}
    extra = f'<script type="application/ld+json">{json.dumps(ld)}</script>\n'
    ing = "\n".join(f"<li>{html.escape(i)}</li>" for i in r["ingredients"])
    steps = "\n".join(f"<li>{html.escape(s)}</li>" for s in r["steps"])
    story = "\n".join(f"<p>{html.escape(p)}</p>" for p in r.get("story", []))
    reel = (f'<blockquote class="instagram-media" data-instgrm-permalink="{r["reel"]}" data-instgrm-version="14">'
            f'<a href="{r["reel"]}">Watch the Reel</a></blockquote>') if r.get("reel") else ""
    write(f'/recipes/{r["slug"]}/', head(r["title"], r["summary"], f'/recipes/{r["slug"]}/', extra)
          + header("/recipes/", page_head(html.escape(r["title"]), html.escape(r["summary"])))
          + f"""<section><div class="wrap prose">
    <p class="note">What works for me with PCOS, not medical advice.{' This post has affiliate links, see the <a href="/disclosure/">disclosure</a>.' if r.get("affiliate") else ''}</p>
    {story}
    {reel}
    <h2>Ingredients</h2>
    <p>Prep {r["prep"]} min · Cook {r["cook"]} min · Serves {r["servings"]}</p>
    <ul>{ing}</ul>
    <h2>Steps</h2>
    <ol>{steps}</ol>
  </div></section>
""" + SIGNUP + footer('<script async src="https://www.instagram.com/embed.js"></script>\n'))

# ---------- Sitemap ----------
paths = ["/", "/recipes/", "/blog/", "/shop/", "/about/", "/work-with-me/", "/disclosure/", "/privacy/"]
paths += [f"/recipes/{r['slug']}/" for r in RECIPES] + [f"/blog/{p['slug']}/" for p in POSTS]
with open("sitemap.xml", "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for p in paths:
        f.write(f"  <url><loc>{SITE}{p}</loc></url>\n")
    f.write("</urlset>\n")
print("built", len(paths), "pages")
