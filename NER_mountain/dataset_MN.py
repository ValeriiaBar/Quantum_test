import pandas as pd

#allcounties.zip from GeoNames was downloaded
print("file is reading...")
file_path = r"C:\Users\Lenovo\Downloads\allCountries\allCountries.txt"
columns = [
    "geonameid", "name", "asciiname", "alternatenames", "latitude", "longitude",
    "feature_class", "feature_code", "country_code", "cc2", "admin1_code",
    "admin2_code", "admin3_code", "admin4_code", "population", "elevation",
    "dem", "timezone", "modification_date"
    ]

#file reading
data = pd.read_csv(file_path, sep="\t", header=None, names=columns, low_memory=False)

#line filtration  by Feature Code, we need: MN - mountains, MNS - mountains, VLC - volkano
filtered_data = data[data["feature_code"].isin(["MT", "MTS", "VLC"])]

#scoosing only usefull columns
mountains_data = filtered_data[["name", "asciiname", "latitude", "longitude", "feature_code"]]

#saving to csv
output_path = "mountains_names.csv"
mountains_data.to_csv(output_path, index=False)

print(f"Файл с горами збережено як {output_path}")
print(mountains_data.head())
