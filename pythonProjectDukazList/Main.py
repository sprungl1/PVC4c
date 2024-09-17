#Je zachovano poradi ve kterem jsou prvky kolekce vkladany?
#Jsou hodnoty ulozene v serazenem poradi od nejmensiho po nejvetsi??
#Je mozne ulozit dva stejné prvky?
#Je mozne vlozit hodnotu None?
mylist = [1,6,6,9,8,2, None]
print(mylist, "Ano zachova")

#Používá se pro přístup k hodnotám index? (Index je systémem vygenerované číslo 0,1,2.. )
print(mylist[1])

#Je možné kolekce vnořovat, tedy vložit jako prvek kolekce další kolekci s několika prvky?
BigList = [mylist, 80]
print(BigList)

#Je možné za běhu programu změnit velikost kolekce?
#Jakymi všemi metodami je možné vložit nový prvek do kolekce a jaké mají tyto metody vstypy?
BigList.append(90)
print(BigList)

#Jakým způsobem zjistím počet prvků v kolekci?
print(len(BigList))

#Jakymi všemi metodami je možné smazat/odebrat existující prvek do kolekce a jaké mají tyto metody vstypy?\
BigList.pop(2)
print(BigList)

#Jakymi všemi metodami je možné upravit hodnotu existujícího prvek v kolekci a jaké mají tyto metody vstypy?
BigList[1] = 99
print(BigList)

#Jakymi všemi metodami je možné ověřit jestli kolekce obsahuje nějaký prvek?
TestList = [1,2,3,4,5]
print(TestList.count(1))
test = 6 in TestList
print(test)
print(TestList.index(4))