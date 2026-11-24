# Content for the site. Add a recipe or post here, then run: python3 _tools/build.py
# Recipe fields: slug, title, summary, prep (min), cook (min), servings, ingredients [..], steps [..],
#   story [paragraphs], reel (Instagram URL), image (/images/x.jpg), date (YYYY-MM-DD), affiliate (bool)
# Post fields: slug, title, summary, date (YYYY-MM-DD), date_label, read, image, blocks [(kind, value, ...)]
#   kinds: ("p", html) ("h", text) ("quote", text) ("yt", video_id, credit_html) ("img", src, alt) ("ask", title, html)
# Only Aanchal's own, approved content goes here.
RECIPES = []

POSTS = [
    {
        "slug": "feminism-in-reverse-sandeep-das-raj-shamani",
        "title": "\"Feminism is ending\"? A working mom reacts to Raj Shamani's podcast",
        "summary": "Sandeep Das told Raj Shamani that women are walking away from feminism and back to traditional roles. I work full time and I'm raising a toddler. Here's where I agree, and where I don't.",
        "date": "2026-11-24",
        "date_label": "November 24, 2026",
        "read": "6 min read",
        "image": "/images/aanchal-kitchen.jpg",
        "blocks": [
            ("p", "A clip from Raj Shamani's <em>Figuring Out</em> podcast has been all over my feed. His guest, author and leadership coach Sandeep Das, says feminism may be coming to an end, and that a lot of women are quietly choosing the \"old\" life again: marriage, kids, a smaller job, home first."),
            ("p", "I'm a mom of a two-year-old. I work full time in home insurance. I go to the gym when I can squeeze it in. So this one hit close to home, and I had to sit down and write about it."),
            ("yt", "MD-IinQ1J3M", "Clip: \"End of Feminism Is Near\" with Sandeep Das, from <a href=\"https://www.figuringout.co/link/fo-525\" rel=\"noopener\">Figuring Out episode 525</a> (Raj Shamani Clips on YouTube)."),
            ("h", "What he actually said"),
            ("p", "In short, his argument goes like this:"),
            ("p", "• Feminism, as he describes it historically, meant a woman could study what she wanted, work where she wanted, and share the labour at home equally.<br>• Now there's a big \"tradwife\" trend in the US. He points to surveys and viral videos where women say they were sold a lie: work crazy hours, skip marriage, skip kids, and you'll be free and happy.<br>• Instead, a lot of them say they ended up lonely and burnt out. They look at their mom's life, a smaller job, a husband, a home to come back to, and think it wasn't so bad.<br>• He predicts the provider-and-nurturer roles will come back, because society moves in waves. And he doesn't think a full role reversal, where the woman provides and the man stays home, will really work, because our subconscious wiring is hard to change."),
            ("h", "Where I agree with him"),
            ("p", "The burnout is real. I see it in my friends and I feel it in myself. Nobody told us that \"having it all\" often means doing it all, at the same time, on four hours of sleep."),
            ("p", "And choosing home is not a failure. I've said this on my page before and I'll keep saying it: being a homemaker is one of the toughest, most underrated jobs out there. If a woman looks at her life and decides family comes first, that is her choice, and it deserves respect, not a lecture."),
            ("p", "Interestingly, Das says this himself in the clip. A woman choosing the traditional life is, in a way, also feminism, because she's the one making the choice."),
            ("h", "Where I don't"),
            ("p", "This is where he loses me. He says that's not really what feminism means, because feminism means becoming a CEO and doing everything alone."),
            ("quote", "That was never the deal. The deal was choice."),
            ("p", "Feminism didn't promise every woman a corner office. It promised that the woman who wants the corner office can go for it, and the woman who wants to be home with her kids can do that too, without anyone deciding for her. My mom's generation often didn't get to choose. That's the difference."),
            ("p", "I also don't buy that roles are fixed in our brains. I work full time. My husband Anuj and I figure out our week together, and it looks different from how our parents did it. It isn't perfect. Some weeks are messy. But it's ours, and it works because we talk about it, not because one of us was wired for it."),
            ("p", "And honestly? The answer to burnout isn't to take women's options away. It's to make the options better: workplaces that don't expect 16-hour days, partners who share the load at home, and families who stop asking <em>log kya kahenge</em> every time a woman makes a decision for herself."),
            ("h", "What I think is really happening"),
            ("p", "I don't think women are rejecting feminism. I think we're rejecting the idea that there is one right way to be a woman, whether that's \"boss babe\" or \"perfect housewife\". Both can turn into a box."),
            ("p", "Real empowerment isn't about competing with men. It's about knowing your worth, whether you're building your own income or running an entire household. No matter which path you choose, someone will question it. So stop explaining, and start owning it."),
            ("ask", "Now I want to hear from you", "Is feminism ending, or just changing? Did you choose career, home, or a messy mix of both? Comment on my latest Reel or email me your story. I'll share the best answers (with your permission) in a follow-up post."),
            ("p", "<small>This post is my personal opinion, reacting to a publicly available podcast clip. Quotes and views are paraphrased from the episode; watch the full conversation for context.</small>"),
        ],
    },
]

# SHOP entries: {"name": ..., "url": affiliate link, "why": one line in her words}. Only products she uses.
SHOP = []
