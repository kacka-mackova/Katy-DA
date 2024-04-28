import json

with open("alice.txt", encoding="utf-8") as file:
    text = file.read()

txt = "".join(text.split())
letters = sorted(list(txt.lower()))

txt_dict = {}

for l in letters:
    if l in txt_dict:
        txt_dict[l] += 1
    else:
        txt_dict[l] = 1

with open("hw01_output.json", mode="w", encoding="utf-8") as output_file:
    json.dump(txt_dict, output_file, indent=4, ensure_ascii=False)
