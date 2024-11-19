def generatorKrasovychJezerCR():
    try:
        yield "Chalupské jezírko"
        yield "Velké mechové jezírko"
        yield "Jezírko pod Táborem"
        yield "Malé mechové jezírko"
    except GeneratorExit:
        print("!Generovani preruseno!")

jezera = generatorKrasovychJezerCR()
print("Krasjova jezera v CR")
while True:
    try:
        jezero = next(jezera)
        if jezero == "Jezírko pod Táborem":
            break
        else:
            print(jezero)
    except StopIteration:
        break