
#Jsou hodnoty ulozene v serazenem poradi od nejmensiho po nejvetsi?
#Je mozne vlozit hodnotu None?
#Je mozne ulozit dva stejné prvky?
thistuple = (1,2,5,5,None)

#Jakymi všemi metodami je možné upravit hodnotu existujícího prvek v kolekci a jaké mají tyto metody vstupy
"""try:
    print(thistuple[1])
    thistuple[1] = 5
except IndexError:
"""
#Jakým způsobem zjistím počet prvků v kolekci?
print(len(thistuple))
#Je možné kolekce vnořovat, tedy vložit jako prvek kolekce další kolekci s několika prvky?
secnondtuple = (thistuple, 69)
print(secnondtuple)
#Používá se pro přístup k hodnotám index? (Index je systémem vygenerované číslo 0,1,2..
#Jakymi všemi metodami je možné získat hodnotu v pořadí třetího prvku v kolekci?
test_indexu = thistuple[3]
print(test_indexu)
#Jakymi všemi metodami je možné smazat/odebrat existující prvek do kolekce a jaké mají tyto metody  vstypy?
#Je možné za běhu programu změnit velikost kolekce
"""thistuple.append(99)""" # 'tuple' object has no attribute 'append'

#Jakymi všemi metodami je možné ověřit jestli kolekce  obsahuje nějaký prvek?
mytuple = (10, 20, 30, 40, 50)
include30 = 30 in mytuple  # Vrátí True
print(include30)
mytuple1 = (1,5,5)
print(mytuple1.count(5))
print(mytuple1.count(6)) # vrátí 0 pokud neobsahuje
mytuple2 = (4,3,2,1)
print(mytuple2.index(1))