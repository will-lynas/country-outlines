import json
import os
import shutil


with open("country_codes.json") as json_file:
    data = json.load(json_file)
    code_dict = {country["code"].lower(): country["name"] for country in data}

continents = {x: x for x in "africa asia europe oceania samerica namerica".split()}
continents["samerica"] = "south_america"
continents["namerica"] = "north_america"

images_dir = "images"
mapsicon_path = "mapsicon"

if not os.path.exists(images_dir):
    os.mkdir(images_dir)

with open("country_outlines_import.csv", "w") as out_file:
    for continent_key in continents.keys():

        codes = os.listdir(os.path.join(mapsicon_path, continent_key))
        for code in codes:

            if code == "index.html":
                continue
            if code not in code_dict:
                raise Exception(f"Code '{code}' not found!")

            out_file.write(f"\"{code_dict[code]}\", ")
            out_file.write(f"<img src=\"country_outlines_{code}.png\">, ")
            out_file.write(f"country_outlines::{continents[continent_key]}")
            out_file.write("\n")

            shutil.copy(
                os.path.join(mapsicon_path, continent_key, code, "512.png"),
                os.path.join(images_dir, f"country_outlines_{code}.png")
            )
