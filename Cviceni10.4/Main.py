vysledky = [
    ("Karel", 31),
    ("Petr", 10),
    ("Honza", 52),
    ("Eva", 61),
    ("Katka", 0),
]

sorted_list =  sorted(vysledky,reverse=(True), key = lambda x:x[1])

print(sorted_list)