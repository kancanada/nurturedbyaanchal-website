import html

REELS = [
    ("DYisdRJMqNF", "A postpartum woman needs her mother", "Step back, sasuma. Not out, just back."),
    ("DYa-MPeMxN0", "Everyone saw the baby. Nobody saw the mom.", "What new moms hear after “pehla pota hai”."),
    ("DV6TkXEDF7R", "That one good day a month", "When your hormones, your hair and your makeup all cooperate."),
    ("DS6UBrmCOUj", "How I see my husband", "A date night on the water with Anuj."),
    ("DM0tD93oZg2", "Welcome to Nurtured by Aanchal", "Where it all started: something soft, something nurturing."),
]


def reel_wall(IG):
    cards = "".join(
        f'''<a class="reel" href="https://www.instagram.com/reel/{rid}/" rel="noopener">
          <span class="reel-img"><img src="/images/reels/{rid}.jpg" alt="Aanchal in her Reel: {html.escape(t)}" loading="lazy"></span>
          <span class="reel-t">{html.escape(t)}</span>
          <span class="reel-c">{html.escape(c)}</span>
        </a>''' for rid, t, c in REELS)
    return cards


def home_html(IG, AVEE, RECIPES, POSTS, photo, NEWS):
    rec = "".join(
        f'<a class="r-card" href="/recipes/{r["slug"]}/"><img src="{r["image"]}" alt="{html.escape(r["title"])}" loading="lazy"><span class="r-meta">{r["prep"] + r["cook"]} min · {html.escape(r.get("cat",""))}</span><h3>{html.escape(r["title"])}</h3></a>'
        for r in RECIPES[:4])
    posts = "".join(
        f'<a class="b-card" href="/blog/{p["slug"]}/"><img src="{p.get("image","/images/aanchal-hero.jpg")}" alt="" loading="lazy"><h3>{html.escape(p["title"])}</h3><p>{html.escape(p["summary"])}</p></a>'
        for p in POSTS[:3])
    return f"""
<section class="s-hero">
  <div class="wrap s-hero-grid">
    <div class="s-hero-text reveal">
      <h1>Strong mama.<br>Soft heart.<br><em>Loud opinions.</em></h1>
      <p class="s-lede">I'm Aanchal: a working mom in Vancouver, raising a toddler, lifting weights and saying the things South Asian women are told to keep quiet.</p>
      <div class="s-proof">
        <div><b data-count="12" data-suffix="M+">12M+</b><span>Reel views</span></div>
        <div><b data-count="382">382</b><span>Reels posted</span></div>
        <div><b data-count="23">23</b><span>Reels past 100K</span></div>
      </div>
      <p class="s-ctas"><a class="btn" href="#story">Read my story</a> <a class="btn btn-ghost-dark" href="/work-with-me/">Work with me</a></p>
    </div>
    <div class="s-hero-photo reveal">{photo("hero", "Aanchal Bathija in a red jacket under winter lights")}</div>
  </div>
  <a class="scroll-cue" href="#story" aria-label="Scroll to my story">Scroll</a>
</section>

<section class="chapters" id="story">
  <div class="wrap">
    <article class="chapter flip reveal">
      <div class="ch-img"><img src="/images/album/wedding-veil.jpg" alt="Aanchal and Anuj on their wedding day under her veil" loading="lazy"></div>
      <div class="ch-text"><span class="ch-no">01</span><h2>It started with us.</h2><p>Anuj and I, our families, and a wedding full of colour. Before the bump, the toddler and the juggle, there was this.</p></div>
    </article>
    <article class="chapter reveal">
      <div class="ch-img"><img src="/images/album/maternity-white.jpg" alt="Aanchal in a white dress during her maternity shoot on a Mexican beach" loading="lazy"></div>
      <div class="ch-text"><span class="ch-no">02</span><h2>First, there was the bump.</h2><p>A full-time job, a growing belly, and a lot of advice from everyone who had an opinion. I didn't know yet how much my life, and I, were about to change.</p></div>
    </article>
    <article class="chapter flip reveal">
      <div class="ch-img"><img src="/images/album/newborn-forest.jpg" alt="Aanchal holding her newborn son in a forest" loading="lazy"></div>
      <div class="ch-text"><span class="ch-no">03</span><h2>Then he arrived, and everything changed.</h2><p>Including how much of me was left at the end of the day. Postpartum is an identity shift nobody prepares you for. I decided my health and my time mattered too.</p></div>
    </article>
    <article class="chapter reveal">
      <div class="ch-img"><img src="/images/aanchal-kitchen.jpg" alt="Aanchal holding her son under festive lights" loading="lazy"></div>
      <div class="ch-text"><span class="ch-no">04</span><h2>Now: the juggle.</h2><p>Home insurance by day. A two-year-old by evening. Workouts squeezed in somewhere. A husband, Anuj, who's in it with me. It isn't perfect, and I don't pretend it is.</p></div>
    </article>
    <article class="chapter flip reveal">
      <div class="ch-img"><img src="/images/album/lunch.jpg" alt="Aanchal smiling" loading="lazy"></div>
      <div class="ch-text"><span class="ch-no">05</span><h2>So I started talking.</h2><p>About mom guilt, marriage, money, <em>log kya kahenge</em>, and the feminism nobody explains properly. It turns out millions of women were thinking the same thing.</p></div>
    </article>
  </div>
</section>

<section class="reels-sec">
  <div class="wrap">
    <div class="reels-head reveal">
      <h2>The conversations women keep sharing</h2>
      <p>Over 12 million Reel views on Instagram, mostly from women who felt seen. Swipe through a few, then come say hi.</p>
    </div>
  </div>
  <div class="reel-track" tabindex="0" aria-label="Most-viewed Reels">{reel_wall(IG)}</div>
  <div class="wrap"><p class="reels-foot"><a class="btn btn-light" href="{IG}" rel="noopener">Watch on Instagram</a></p></div>
</section>

<section class="latest">
  <div class="wrap">
    <div class="latest-head reveal"><h2>The longer version</h2><a href="/blog/">All posts</a></div>
    <p class="sec-lede">A Reel is 60 seconds. On the blog I say the rest, and I ask for your side of the story.</p>
    <div class="b-grid">{posts}</div>
  </div>
</section>

<section class="kitchen">
  <div class="wrap">
    <div class="kitchen-grid">
      <div class="reveal"><img class="k-photo" src="/images/album/eat-pizza.jpg" alt="Aanchal smiling over pizza night" loading="lazy"></div>
      <div class="reveal"><h2>And yes, we still have to eat.</h2><p>Quick South Asian weeknight dinners and toddler meals that survive real life.</p><a class="btn" href="/recipes/">See the recipes</a></div>
    </div>
    <div class="r-grid" style="margin-top:44px">{rec}</div>
  </div>
</section>

<section class="brands">
  <div class="wrap brands-grid">
    <div class="reveal">
      <h2>For brands</h2>
      <p>A real working mom with a highly engaged audience of women who argue in the comments, save, and share. I make UGC that brands run as ads, plus Reels, recipe posts and newsletter features.</p>
      <p class="proof-line">Recent work: a paid UGC video for <a href="{AVEE}" rel="noopener">Avee Health</a>, which they ran as an ad.</p>
      <a class="btn btn-light" href="/work-with-me/">Work with me</a>
    </div>
    <div class="brand-stats reveal">
      <div><b data-count="3.6" data-suffix="M" data-dec="1">3.6M</b><span>views on my top Reel</span></div>
      <div><b data-count="12" data-suffix="M+">12M+</b><span>total Reel views</span></div>
      <div><b data-count="42">42</b><span>Reels past 10K views</span></div>
      <div><b>YVR</b><span>Vancouver-based, working across Canada &amp; the US</span></div>
    </div>
  </div>
</section>

{NEWS}"""
