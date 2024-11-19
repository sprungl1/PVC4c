


def vydej_obedu():
    menu = [
         "vitamínový nápoj",
         "polévka česneková s bramborem",
         "segedínský guláš, houskové knedlíky",
         "jablko",
    ]
    A = ["řízek"]
    B = ["polévka"]
    yield menu[0]
    print( "Co si dáte A nebo B")
    odpoved = yield
    if (odpoved) == "A":
        yield A
    elif (odpoved) == "B":
        yield B


corutina1 = vydej_obedu()
napoje = next(corutina1)
print(napoje)
next(corutina1)
print(corutina1.send("A"))

corutina1.close()





