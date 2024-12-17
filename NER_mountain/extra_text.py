sentences = [
    "Mount Everest, the tallest peak on Earth, attracts climbers from around the world.",
    "K2, known for its extreme difficulty, is one of the most dangerous mountains to climb.",
    "Kangchenjunga, located between Nepal and India, is the third highest mountain in the world.",
    "Mount Kilimanjaro, with its snow-capped summit, is a famous hiking destination in Tanzania.",
    "Mount Fuji, a sacred symbol in Japan, is renowned for its symmetrical cone shape.",
    "Mont Blanc, the highest mountain in the Alps, draws mountaineers every year.",
    "The iconic Matterhorn stands as one of the most recognizable peaks in the Swiss Alps.",
    "Mount Denali, the highest peak in North America, offers a challenging ascent for mountaineers.",
    "Mount Elbrus, located in the Caucasus Mountains, is the highest mountain in Europe.",
    "Mount Makalu, part of the Himalayas, is known for its steep slopes and remote location.",
    "Lhotse, closely connected to Mount Everest, is the fourth highest mountain in the world.",
    "Cho Oyu is a popular choice for climbers looking to conquer an 8,000-meter peak.",
    "Dhaulagiri is a massive peak in the Himalayas, towering over Nepal’s mountainous landscape.",
    "Annapurna is infamous for its deadly avalanche-prone slopes, making it one of the hardest mountains to summit.",
    "Mount St. Helens erupted in 1980, reshaping the surrounding landscape and ecology.",
    "Mount Vesuvius, known for its eruption that destroyed Pompeii, remains an active volcano.",
    "Mount Pinatubo’s eruption in 1991 caused one of the largest volcanic events of the 20th century.",
    "Mount Etna is Europe’s most active volcano, continuously shaping the landscape of Sicily.",
    "Mount Ararat, located in Turkey, is traditionally considered the resting place of Noah’s Ark.",
    "Mount Aconcagua is the highest peak in the Americas, reaching 6,961 meters.",
    "Mount Rainier’s snow-covered summit is a striking feature of the Pacific Northwest.",
    "Mount Pikes Peak, famous for inspiring Katharine Lee Bates’ song, rises over Colorado Springs.",
    "Mount Rushmore is a monumental sculpture of four U.S. presidents carved into the granite rock.",
    "Mount Kosciuszko is Australia’s highest peak, standing at 2,228 meters above sea level.",
    "Mount McKinley, now known as Denali, is renowned for its towering height and extreme weather.",
    "Mount Hood is a prominent volcano near Portland, Oregon, known for its skiing resorts.",
    "Mount Hermon is the highest point in Syria, with its snow-covered slopes providing skiing opportunities.",
    "Mount Erebus, an active volcano in Antarctica, has one of the world’s longest continuous eruptions.",
    "Mount Whitney, located in California’s Sierra Nevada, is the highest point in the contiguous U.S.",
    "Mount Shasta’s volcanic peak stands as a prominent feature in northern California’s landscape.",
    "Mount McKinley, also known as Denali, has been a challenging summit for mountaineers.",
    "Mount Olympus, in Greece, is steeped in myth as the home of the ancient gods.",
    "Mount Assiniboine, often referred to as the 'Matterhorn of the Rockies,' is a stunning sight in Canada.",
    "Mount of the Holy Cross in Colorado is named for the cross-shaped snowfield visible on its slopes.",
    "Ben Nevis is the highest mountain in the United Kingdom, located in Scotland.",
    "Mount Etna, with its frequent eruptions, is one of the world’s most active volcanoes.",
    "Mount Meru, located in Tanzania, is an active volcano and the second highest mountain in the country.",
    "Mount Taranaki in New Zealand is an iconic, symmetrical stratovolcano.",
    "Mount Cook, or Aoraki, is New Zealand’s highest mountain, surrounded by rugged landscapes.",
    "Mount Kenya, with its glacier-capped peaks, is the second highest mountain in Africa.",
    "Table Mountain in Cape Town is famous for its flat top and panoramic views.",
    "Mount Toubkal, in Morocco, is the highest mountain in North Africa.",
    "Mount Fitz Roy, located on the border between Argentina and Chile, is known for its rugged granite peaks.",
    "Mount Roraima is a massive tabletop mountain in South America, shared by Venezuela, Brazil, and Guyana.",
    "Mount Vinson, located in Antarctica, is the highest peak on the continent.",
    "Mount Tambora erupted in 1815, causing the 'Year Without a Summer' due to the volcanic ash cloud.",
    "Mount Ruinsori, known as the 'Mountains of the Moon,' rises between Uganda and the Democratic Republic of the Congo.",
    "Shishapangma is one of the 14 peaks in the Himalayas that rise over 8,000 meters.",
    "Mount Derenik is a lesser-known peak nestled within the Himalayas of India.",
    "Ras Dashen, located in the Simien Mountains of Ethiopia, is the country’s highest peak.",
    "Mount Bromo, an active volcano in Indonesia, is famous for its dramatic caldera and views.",
    "Mount Ruinsori’s glaciers and snow-capped peaks offer a challenging climb in Central Africa.",
    "Cerro Torre, located in Patagonia, is known for its needle-like spire and difficulty to summit.",
    "Mount Teide is Spain’s highest peak, located on the Canary Islands and an active volcano.",
    "Mount Bezimiany, located in Russia, is an active stratovolcano with frequent eruptions.",
    "Mount Elbrus is often considered the highest mountain in Europe, located in the Caucasus.",
    "Mount Fuji is an iconic symbol of Japan, attracting thousands of hikers every year.",
    "Mount Lenana is a challenging peak in Mount Kenya National Park.",
    "Mount Chimborazo, despite not being the highest mountain, is the farthest point from the Earth’s center.",
    "Mount Pisco is one of the popular trekking peaks in the Peruvian Andes.",
    "Ojos del Salado, located on the Chile/Argentina border, is the highest active volcano in the world.",
    "Mount Chandrashila, in India, offers panoramic views of the Himalayan range.",
    "Mount Hakkoda, in Japan, is known for its harsh winters and beautiful ski resorts.",
    "Mount Ord, in Australia, offers breathtaking views of the surrounding outback.",
    "Mount Mashu, located in Japan, is famous for its crater lake and fog-covered slopes.",
    "Mount Montois, located in the French Alps, is often a favorite among mountaineers.",
    "Vaalserberg, located in the Netherlands, is the highest point in the country.",
    "Annapurna is infamous for its dangerous climbing routes and frequent avalanches.",
    "Mount Baimen, located in China, remains a relatively unexplored destination for climbers.",
    "Amadablam, often referred to as the 'Matterhorn of the Himalayas,' is a challenging peak to climb.",
    "Mamlambo, located in South Africa, offers a unique landscape for trekkers.",
    "Kilimanjaro’s diverse ecosystems attract hikers from around the world.",
    "Mount Longonot is a dormant volcano in Kenya that offers an excellent hiking experience.",
    "Mount Ngong, part of the Ngong Hills in Kenya, offers lush green views and hiking trails.",
    "Mount Meru, located in Tanzania, is an active volcano and the second highest mountain in the country.",
    "Thabana, located in South Africa, is known for its stunning views and hiking opportunities.",
    "The Zillertal Alps in Austria are known for their towering peaks and excellent ski resorts.",
    "The foothills of the Himalayas provide a unique entry point for those aiming for higher summits.",
    "Pic de Bugarach, located in France, is a mysterious mountain surrounded by many local legends.",
    "Mount St. Francis, located in the United States, is known for its challenging climbing routes.",
    "Vesuvius, famous for its eruption that destroyed Pompeii, continues to be an active threat.",
    "Agung is an active volcano in Bali, Indonesia, with a significant cultural and spiritual importance.",
    "Fitz Roy is a striking peak in Patagonia, renowned for its dramatic granite cliffs.",
    "Jaya, located in Indonesia, is the highest peak in Oceania.",
    "The ascent of Mount Kilimanjaro is a bucket-list adventure for many trekkers.",
    "Mount Etna, constantly erupting, has shaped the landscape of Sicily for millennia.",
    "The Ruinsori Mountains are known for their unique flora and fauna, often called the 'Mountains of the Moon.'",
    "Zillertal Alps offer some of the best alpine skiing and mountaineering opportunities in Austria.",
    "Mount Garibaldi, located in British Columbia, offers striking volcanic landscapes.",
    "Mount Doom, famous from the Lord of the Rings, is a fictional location based on real volcanoes.",
    "Mount Paget, located on South Georgia Island, is the highest peak on the island.",
    "Taranaki is a dormant volcano surrounded by lush forests in New Zealand.",
    "Torok is a lesser-known but impressive peak located in Siberia.",
    "Mount Koyasan, known for its Buddhist temples, is a spiritual site in Japan.",
    "Fitzroy is renowned for its steep granite faces and challenging climbs.",
    "Wu, located in China, is famous for its tranquil beauty and ancient temples.",
    "Zermatt is famous for its mountaineering and ski resorts, with Matterhorn visible from the town."
]

output_file = "extra100_texts.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for text in sentences:
        f.write(text + "\n")

print(f"Generated texts saved to {output_file}")