#Je zachovano poradi ve kterem jsou prvky kolekce  vkladany?
from unicodedata import numeric

mySet = {"gun" , "shovel" , "truck"}
print(mySet)
#Ne u Stringu
#Jsou hodnoty ulozene v serazenem poradi od nejmensiho po nejvetsi
#Je mozne ulozit dva stejné prvky?
#Je mozne vlozit hodnotu None?
NumSet = {1,2,2,3,10,6,None}
print(NumSet)

#Používá se pro přístup k hodnotám index? (Index je systémem vygenerované číslo 0,1,2.. )
"""print(NumSet[2])"""
#Je možné kolekce vnořovat, tedy vložit jako prvek kolekce další kolekci s několika prvky?
"""TSet = {NumSet, 80}
print(TSet)"""
#Je možné za běhu programu změnit velikost kolekce?
NumSet.remove(1)
print(NumSet)

#Jakým způsobem zjistím počet prvků v kolekci?
print(len(NumSet))
#Jakymi všemi metodami je možné vložit nový prvek do kolekce a jaké mají tyto metody vstypy?
NumSet.add(69)
print(NumSet)

#Jakymi všemi metodami je možné smazat/odebrat existující prvek do kolekce a jaké mají tyto metody vstypy?
NumSet.remove(69)
print(NumSet)
my_set = {1, 2, 3}
my_set.discard(2)
my_set.clear()  # Vyprázdní množinu

# Jakymi všemi metodami je možné upravit hodnotu  existujícího prvek v kolekci a jaké mají tyto metody  vstypy?
"""TestS = {5,6}
TestS[1] = 10
print(TestS)"""

# Jakymi všemi metodami je možné ověřit jestli kolekce  obsahuje nějaký prvek?
testSet = {1, 2, 3}
if 2 in testSet:
    print("Prvek 2 je v množině")

    my_set = {1, 2, 3}
    other_set = {1, 2}
    if other_set.issubset(my_set):
        print("Všechny prvky other_set jsou v my_set")

my_set = {1, 2, 3}
other_set = {1, 2}
if my_set.issuperset(other_set):
    print("my_set obsahuje všechny prvky z other_set")
