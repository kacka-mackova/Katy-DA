"""Spočítej celkový počet všech znaků (včetně mezer, netisknutelných a neviditelných znaků) ve sloupci PRIMARYTITLE ze 
souboru netflix_imdb_test.tsv. 
Výsledek má být: 7650. Pošli nám jako odpověď python soubor."""

netflix = []
with open("netflix_imdb_test.tsv", encoding="utf-8") as output_file:
    for row in output_file:
        netflix.append(row.split("\t"))

# columns primarytitle without header
column_primarytitle = []
for row in netflix[1:]:
    column_primarytitle.append(row[2])

list_of_charaters = list("".join(column_primarytitle))

count_of_characters = 0
for character in list_of_charaters:
    count_of_characters += 1
print(f"Celkový počet znaků ve sloupci PrimaryTitles je: {count_of_characters}")
