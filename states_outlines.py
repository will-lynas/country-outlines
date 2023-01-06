import json
import os
import shutil

with open("states_codes.json") as json_file:
    code_dict = json.load(json_file)
    code_dict = {key.lower(): value for key, value in code_dict.items()}

images_dir = "images"
mapsicon_path = "mapsicon"
us_path = os.path.join(mapsicon_path, "us")

if not os.path.exists(images_dir):
    os.mkdir(images_dir)

with open("states_outlines_import.csv", "w") as out_file:

    codes = os.listdir(us_path)
    for code in codes:

        if code in ["index.html", "us"]:
            continue
        if code not in code_dict:
            raise Exception(f"Code '{code}' not found!")

        out_file.write(f"\"{code_dict[code]}\", ")
        out_file.write(f"<img src=\"states_outlines_{code}.png\">")
        out_file.write("\n")

        shutil.copy(
            os.path.join(us_path, code, "512.png"),
            os.path.join(images_dir, f"states_outlines_{code}.png")
        )
