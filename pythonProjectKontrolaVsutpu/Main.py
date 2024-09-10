from logging import exception
b = 0
while b == 0:
    try:
        x = input("Zadej cislo: ")
        y = int(x) + 1
        print(y)
        b = +1

    except ValueError:
        print("Zadejte Číslo")
        b = 0
