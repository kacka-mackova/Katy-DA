import json

titles = []
with open("netflix_titles.tsv", encoding="utf-8") as output_file:
    for line in output_file:
        title = line.split("\t")
        titles.append(title)

title_index = titles[0].index("PRIMARYTITLE")
director_index = titles[0].index("DIRECTOR")
cast_index = titles[0].index("CAST")
genre_index = titles[0].index("GENRES")
decade_index = titles[0].index("STARTYEAR")

titles_dict = []
for value in titles[1:]:
    new_dict = {}
    for key in value:
        new_dict["title"] = value[title_index]
        new_dict["directors"] = value[director_index].split(", ")
        new_dict["cast"] = value[cast_index].split(", ")
        new_dict["genres"] = value[genre_index].split(",")
        new_dict["decade"] = int(value[decade_index][:3] + "0")
    for key, value in new_dict.items():
        if value == [""]:
            new_dict[key] = []
    titles_dict.append(new_dict)


with open("hw02_output.json", mode="w", encoding="utf-8") as output_file:
    json.dump(titles_dict, output_file, indent=4, ensure_ascii=False)
