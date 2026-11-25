import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from content import RECIPES
from recipe_extras import EXTRAS
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

OLIVE = colors.HexColor("#666640"); SLATE = colors.HexColor("#5F7A8B"); LIME = colors.HexColor("#EEF5C2"); INK = colors.HexColor("#2f2f1e")
H1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=30, leading=34, textColor=INK, spaceAfter=10)
H2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=19, leading=23, textColor=OLIVE, spaceBefore=6, spaceAfter=8)
H3 = ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=12, leading=15, textColor=SLATE, spaceBefore=8, spaceAfter=4)
B = ParagraphStyle("b", fontName="Helvetica", fontSize=11, leading=16, textColor=INK, spaceAfter=6)
S = ParagraphStyle("s", parent=B, fontSize=9.5, leading=13, textColor=colors.HexColor("#555544"))
by = {r["slug"]: r for r in RECIPES}

def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;")

def footer(c, d):
    c.saveState(); c.setFont("Helvetica", 8.5); c.setFillColor(OLIVE)
    c.drawString(0.75*inch, 0.5*inch, "Nurtured by Aanchal  |  nurturedbyaanchal.com  |  @nurturedbyaanchal")
    c.drawRightString(7.75*inch, 0.5*inch, str(d.page)); c.restoreState()

doc = SimpleDocTemplate("guides/weeknight-dinner-plan.pdf", pagesize=letter, leftMargin=0.75*inch, rightMargin=0.75*inch,
                        topMargin=0.75*inch, bottomMargin=0.8*inch, title="The Working Mom's Weeknight Dinner Plan", author="Aanchal Bathija")
st = []
st += [Image("images/aanchal-kitchen.jpg", width=7*inch, height=4.2*inch, kind="proportional"), Spacer(1, 18),
       Paragraph("The Working Mom's Weeknight Dinner Plan", H1),
       Paragraph("One week of South Asian dinners that fit around a full-time job and a toddler. Shopping list, plan and 8 recipes inside.", B),
       Spacer(1, 10),
       Paragraph("Hi, I'm Aanchal. I work full time in home insurance, I'm raising a two-year-old, and I still want us to sit down to a real dinner most nights. "
                 "This is the plan I actually use: one Sunday cook, quick weeknights, and toddler portions pulled out before the chilli goes in.", B),
       PageBreak()]

plan = [("Sunday", "sunday-rajma-chawal", "Big pot. Freeze half for next week."),
        ("Monday", "easy-chana-masala-instant-pot", "Make extra for Tuesday's lunchbox."),
        ("Tuesday", "weeknight-moong-dal-tadka", "30 minutes, no soaking."),
        ("Wednesday", "paneer-bhurji-lunchbox-wrap", "Dinner tonight, wraps for tomorrow."),
        ("Thursday", "dry-aloo-gobi-sabzi", "With dal from Tuesday or roti."),
        ("Friday", "one-pot-vegetable-khichdi-toddler", "One pot, everyone eats the same thing."),
        ("Saturday", "mini-besan-chilla-toddler-finger-food", "Breakfast-for-dinner night."),
        ("Any morning", "vegetable-upma-breakfast", "20-minute warm breakfast.")]
rows = [["Day", "What we eat", "Time", "Note"]] + [[d, Paragraph(esc(by[s]["title"]), S), f'{by[s]["prep"]+by[s]["cook"]} min', Paragraph(n, S)] for d, s, n in plan]
t = Table(rows, colWidths=[1.0*inch, 2.6*inch, 0.7*inch, 2.7*inch])
t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), OLIVE), ("TEXTCOLOR", (0,0), (-1,0), colors.white), ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 9.5), ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIME]), ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7)]))
st += [Paragraph("Your week at a glance", H2), t, Spacer(1, 16),
       Paragraph("How I make it work", H3)]
for tip in ["Sunday: soak the rajma Saturday night, cook it Sunday, and chop onions for the first half of the week.",
            "Keep canned chickpeas, frozen peas and a block of paneer on hand. They save most weeknights.",
            "Pull out a toddler bowl before adding chilli. One pot, two spice levels.",
            "Leftovers are lunch. Every dinner here packs well for work the next day."]:
    st.append(Paragraph("• " + tip, B))
st.append(PageBreak())

pantry = {"Lentils, beans & grains": ["Yellow moong dal", "Dried rajma (kidney beans)", "Canned chickpeas (2 cans)", "Basmati rice", "Fine semolina (rava)", "Besan (chickpea flour)"],
          "Fresh": ["Onions (6–8)", "Tomatoes (8–10)", "Potatoes (3–4)", "1 cauliflower", "Ginger and garlic", "Green chillies", "Coriander", "Lemons", "Carrots, peas, beans, zucchini", "Paneer (200–250 g)", "Rotis or wraps"],
          "Spices": ["Cumin seeds", "Mustard seeds", "Turmeric", "Kashmiri chilli powder", "Coriander powder", "Garam masala", "Amchur", "Hing", "Curry leaves", "Kasuri methi"],
          "Fats": ["Ghee", "Neutral oil"]}
st.append(Paragraph("Shopping list", H2))
for k, items in pantry.items():
    st.append(Paragraph(k, H3))
    cells = []
    for i in items: cells += ["", Paragraph(esc(i), S)]
    while len(cells) % 6: cells.append("")
    rows = [cells[j:j+6] for j in range(0, len(cells), 6)]
    tb = Table(rows, colWidths=[0.16*inch, 2.12*inch]*3, rowHeights=0.28*inch)
    sty = [("VALIGN", (0,0), (-1,-1), "MIDDLE"), ("LEFTPADDING", (0,0), (-1,-1), 4)]
    for ri, row in enumerate(rows):
        for ci in range(0, 6, 2):
            if row[ci+1] != "":
                sty.append(("BOX", (ci, ri), (ci, ri), 0.8, OLIVE))
    tb.setStyle(TableStyle(sty)); st.append(tb)
st.append(PageBreak())

for d, s, n in plan:
    r = by[s]; x = EXTRAS.get(s, {})
    st.append(Paragraph(esc(r["title"]), H2))
    st.append(Paragraph(f'{d}  |  Prep {r["prep"]} min  |  Cook {r["cook"]} min  |  Serves {r["servings"]}', S))
    st.append(Paragraph(esc(r["summary"]), B))
    st.append(Paragraph("Ingredients", H3))
    for i in r["ingredients"]: st.append(Paragraph("• " + esc(i), B))
    st.append(Paragraph("Method", H3))
    for k, step in enumerate(r["steps"], 1): st.append(Paragraph(f"{k}. " + esc(step), B))
    if x.get("tips"):
        st.append(KeepTogether([Paragraph("My tip", H3), Paragraph(esc(x["tips"][0]), B)]))
    st.append(PageBreak())

st += [Paragraph("Made one of these?", H1),
       Paragraph("Tag @nurturedbyaanchal on Instagram. I'd love to see your table, and I share my favourites.", B),
       Paragraph("More recipes and my posts on motherhood, marriage and working-mom life are at nurturedbyaanchal.com.", B)]
doc.build(st, onFirstPage=footer, onLaterPages=footer)
print("ok")
