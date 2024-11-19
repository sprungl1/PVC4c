def generatorKrasovychJezerCR():
    try:
        yield "Chalupské jezírko"
        yield "Velké mechové jezírko"
        yield "Jezírko pod Táborem"
        yield "Malé mechové jezírko"
    except GeneratorExit:
        print("!Generovani preruseno!")

print("Krasjova jezera v CR")
for jezero in generatorKrasovychJezerCR():
    if jezero == "Jezírko pod Táborem":
        break
    else:
        print(jezero)