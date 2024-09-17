import datetime


def kontrola_data_narozeni(rok, mesic, den):
    aktualni_rok = datetime.datetime.now().year

    # Kontrola roku
    if rok > aktualni_rok or rok < (aktualni_rok - 119):
        raise Exception("Rok musí být mezi {} a {}.".format(aktualni_rok - 119, aktualni_rok))

    # Kontrola měsíce
    if mesic < 1 or mesic > 12:
        raise Exception("Měsíc musí být číslo od 1 do 12.")

    # Kontrola dne podle měsíců
    if mesic in [1, 3, 5, 7, 8, 10, 12]:
        max_den = 31
    elif mesic == 2:
        max_den = 29
    else:
        max_den = 30

    if den < 1 or den > max_den:
        raise Exception("Den musí být mezi 1 a {} pro měsíc {}.".format(max_den, mesic))

    # Kontrola letních prázdnin (1.7. - 31.8.)
    datum = datetime.date(rok, mesic, den)
    prazdniny_zacatek = datetime.date(rok, 7, 1)
    prazdniny_konec = datetime.date(rok, 8, 31)

    if prazdniny_zacatek <= datum <= prazdniny_konec:
        raise Exception("Datum narození nesmí spadat do letních prázdnin (1.7. - 31.8.).")

    print("Datum narození je validní.")



try:
    rok = int(input("Zadejte rok narození: "))
    mesic = int(input("Zadejte měsíc narození: "))
    den = int(input("Zadejte den narození: "))

    kontrola_data_narozeni(rok, mesic, den)

except Exception as e:
    print(f"Chyba: {e}")
