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

TestS = {5,6}
TestS[1] = 10
print(TestS)