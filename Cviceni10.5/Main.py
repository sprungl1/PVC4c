zbozi = [
    {
        "name" : "IPHONE 14",
        "price" : 22169.0,
        "category" : (12, "Mobilní telefony")
    },
    {
        "name" : "Fujifilm XT30",
        "price" : 22269.0,
        "category" : (2, "Fotoaparáty")
    },
    {
        "name" : "Niceboy HIVE Pins Black",
        "price" : 999.0,
        "category" : (4, "Sluchátka")
    }
]

podle_ceny_vzestupne = sorted(zbozi, key=lambda z: z["price"])

print(podle_ceny_vzestupne)

podle_nazvu_ses = sorted(zbozi,key=lambda z: z["name"])

print(podle_nazvu_ses)

podle_kategorie = sorted(zbozi, key=lambda z: z["category"])

print(podle_kategorie)