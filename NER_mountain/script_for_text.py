import pandas as pd
import random

#part of the code devoted to analysing the received dataset and preparing for text generation
pd.set_option('display.max_columns', None)

data_mountain = pd.read_csv("mountains_names.csv")
print(data_mountain.shape)
#print(data_mountain.head(10))
print(data_mountain['name'].duplicated().sum())
duplicates = data_mountain[data_mountain.duplicated()]
print(duplicates)

data_mountain = data_mountain.drop_duplicates()
print(data_mountain.shape)

print(data_mountain.isnull().sum())
#creating of the list with all mountains names
mountain_names = data_mountain['name'].unique().tolist()
#print(mountain_names[:100])

#text generation
#examples of text patterns
templates = [
    "The majestic {mountain} attracts thousands of visitors every year.",
    "{mountain} is located in {location} and is known for its breathtaking views.",
    "Climbing {mountain} is a dream for many adventurers around the world.",
    "{mountain} and {mountain2} are popular destinations for trekking enthusiasts.",
    "The {mountain} range offers stunning landscapes and diverse wildlife.",
    "From the peak of {mountain}, one can see {sight} in the distance.",
    "The challenging ascent of {mountain} requires both skill and determination.",
    "{mountain} is an iconic symbol of {location} and a UNESCO World Heritage Site.",
    "Many stories and legends surround {mountain}, making it a cultural treasure.",
    "The area around {mountain} is rich in flora and fauna, attracting nature lovers.",
    "Adventure seekers flock to {mountain}, drawn by its reputation for treacherous climbs.",
    "Located in {location}, {mountain} is a natural wonder that captivates tourists and locals alike.",
    "The summit of {mountain} offers panoramic views of the surrounding valleys and peaks.",
    "The mystical allure of {mountain} has inspired poets, artists, and explorers throughout history.",
    "For centuries, {mountain} has been a destination for those seeking spiritual enlightenment.",
    "The history of mountaineering on {mountain} is filled with remarkable stories of bravery and perseverance.",
    "As the sun sets, {mountain} transforms into a breathtaking sight, with vibrant colors filling the sky.",
    "Whether you're a seasoned mountaineer or a first-time climber, {mountain} offers something for everyone.",
    "The slopes of {mountain} are home to some of the world's most challenging skiing and snowboarding conditions.",
    "Known for its harsh weather and towering heights, {mountain} is a formidable challenge for even the most experienced climbers.",
    "The presence of {mountain} in {location} has shaped the local culture and economy for centuries.",
    "Tourists visiting {mountain} are often left in awe of its sheer size and the surrounding natural beauty.",
    "The paths leading up to {mountain} are marked by ancient stone structures, providing a glimpse into the area's rich history.",
    "While many attempt to conquer {mountain}, few are able to reach its treacherous peak.",
    "The base of {mountain} is a popular spot for camping, hiking, and outdoor activities, attracting nature lovers year-round.",
    "Once you reach the summit of {mountain}, the entire region unfolds before you in a spectacular view.",
    "Trekking through the {mountain} region exposes visitors to unique ecosystems and rare wildlife.",
    "In the winter, {mountain} becomes a paradise for snow sports enthusiasts, with pristine powder covering the slopes.",
    "The harsh conditions of {mountain} make it one of the most challenging environments for both climbers and wildlife.",
    "The summit of {mountain} is often shrouded in mist, adding to its mysterious and awe-inspiring aura.",
    "Every year, adventurers from around the world gather to take on the challenge of reaching the summit of {mountain}.",
    "The quiet beauty of {mountain} offers a peaceful retreat for those looking to escape the hustle and bustle of city life.",
    "As you ascend {mountain}, the air grows thinner, making each step a true test of stamina and determination.",
    "Legends of mythical creatures are said to dwell in the remote areas surrounding {mountain}, adding an air of mystery to the region.",
    "Many tourists visit {mountain} to witness the first light of dawn from its summit, a truly magical experience.",
    "The cultural significance of {mountain} is immense, with local traditions and ceremonies deeply rooted in its presence.",
    "Climbing {mountain} is not only a physical challenge but also a spiritual journey for those who embark on it.",
    "The weather on {mountain} can change rapidly, making preparation and caution essential for any climber.",
    "In the heart of {location}, {mountain} stands as a silent witness to the passage of time and the ever-changing landscape."
]


# Additional data for context generation
locations = [
    "Nepal", "Tanzania", "Alaska", "Switzerland", "Japan",
    "Peru", "New Zealand", "Chile", "Norway", "Canada",
    "Argentina", "Australia", "Iceland", "India", "Bhutan",
    "Mexico", "South Africa", "Himalayas", "Andes", "Rocky Mountains",
    "Siberia", "Greenland", "Mauritius", "Borneo", "Costa Rica",
    "Patagonia", "Scotland", "Austria", "Ethiopia", "Mongolia"
]

sights = [
    "a vast valley", "the nearby lake", "a dense forest", "snow-capped peaks", "rolling hills",
    "crystal-clear waterfalls", "the expansive desert", "a tranquil river", "the rugged coastline",
    "ancient ruins", "endless fields of wildflowers", "vast glaciers", "dense jungles", "a pristine beach",
    "breathtaking cliffs", "a remote island", "a field of volcanic craters", "the glowing aurora borealis",
    "a canyon carved by rivers", "a secluded mountain pass", "a peaceful meadow", "a dense bamboo forest",
    "majestic cliffs overlooking the sea", "the glowing red sands", "the towering cliffs of the fjords",
    "a lush rainforest", "an alpine lake surrounded by towering peaks", "a vibrant coral reef",
    "snowy plateaus", "an ancient temple perched on a mountain", "a hidden valley of wild animals"
]


generated_texts = []
for _ in range(1000):
    template = random.choice(templates)
    text = template.format(
        mountain=random.choice(mountain_names),
        mountain2=random.choice(mountain_names),
        location=random.choice(locations),
        sight=random.choice(sights),
    )
    generated_texts.append(text)

# saving to file
output_file = "generated_texts.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for text in generated_texts:
        f.write(text + "\n")

print(f"Generated texts saved to {output_file}")

