"""Deals page data. Source: Prospecting Agent dashboard (Andy), 2026-11-24.
Only brands with a creator/affiliate program. `deal` stays None until Aanchal has a real code;
`link` is the plain brand site until the affiliate link is connected."""
DEALS = [
 # name, category group, city, what they make, site, program, deal
 ("Loulou Lollipop", "Toddler", "Richmond, BC", "Muslin swaddles, bibs and toddler essentials.", "https://louloulollipop.ca", "Ambassador program", "10% code coming"),
 ("mini mioche", "Toddler", "Toronto, ON", "GOTS organic cotton clothes for babies to adults, made in Canada.", "https://minimioche.com", "Fammbassador program", None),
 ("Mabel's Labels", "Toddler", "Hamilton, ON", "Waterproof name labels for daycare bottles, clothes and gear.", "https://mabelslabels.com", "Affiliate program", None),
 ("Aleva Naturals", "Toddler", "Ontario", "Natural, vegan skincare for babies and moms.", "https://www.alevanaturals.com", "Ambassador & affiliate program", None),
 ("ATTITUDE", "Home", "Montreal, QC", "Vegan body care, laundry and cleaning for the whole family.", "https://attitudeliving.com", "Ambassador Club", None),
 ("Graydon", "Mom", "Toronto, ON", "Made-in-Canada natural skincare for sensitive skin.", "https://graydonskincare.ca", "Skin Squad", None),
 ("Three Ships", "Mom", "Toronto, ON", "Plant-based Canadian skincare.", "https://www.threeshipsbeauty.ca", "Influencer & affiliate program", None),
 ("Blume", "Mom", "Vancouver, BC", "Clean skincare and mineral SPF.", "https://www.blume.com", "Blume Insiders", None),
 ("Elate", "Mom", "Victoria, BC", "Vegan, low-waste cosmetics.", "https://elatebeauty.com", "Affiliate program", None),
 ("Nudestix", "Mom", "Toronto, ON", "Multi-use makeup sticks for two-minute mornings.", "https://www.nudestix.ca", "Nude Squad", None),
 ("DivaCup", "Mom", "Kitchener, ON", "Reusable menstrual cups and discs.", "https://divacup.com", "DIVA Community", None),
 ("Aisle", "Mom", "Vancouver, BC", "Leakproof period underwear and reusable pads.", "https://periodaisle.com", "Ambassador program", None),
 ("Knix", "Mom", "Toronto, ON", "Leakproof underwear and activewear.", "https://knix.ca", "Ambassador program", None),
 ("DUER", "Mom", "Vancouver, BC", "Stretch performance jeans for commuting and everyday.", "https://duer.com/en-ca", "Affiliate program", None),
 ("Encircled", "Mom", "Toronto, ON", "Versatile, Canadian-made travel and everyday clothing.", "https://encircled.ca", "Affiliate HQ", None),
 ("SweetLegs", "Fitness", "Kelowna, BC", "Leggings and apparel.", "https://www.sweetlegs.ca", "Ambassador program", None),
 ("Botanica", "Fitness", "Vancouver, BC", "Plant protein, greens and herbal supplements.", "https://botanicahealth.com", "Affiliate program", None),
 ("Organika", "Fitness", "Richmond, BC", "Collagen and natural health supplements.", "https://organika.com", "Live Healthy Crew", None),
 ("Vega", "Fitness", "Burnaby, BC", "Plant-based protein powders.", "https://myvega.com", "Affiliate program", None),
 ("WildBird", "Toddler", "US", "Baby carriers and ring slings.", "https://wildbird.co", "Affiliate program", None),
]
GROUPS = [("Toddler", "For the little one"), ("Mom", "For mom"), ("Fitness", "Fitness & nutrition"), ("Home", "Home")]
