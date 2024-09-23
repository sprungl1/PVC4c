#Je zachováno pořadí, ve kterém jsou prvky kolekce vkládány?
my_string = "hello", "goodbye"
print(my_string)  # Výstup: ('hello', 'goodbye')

#Jsou hodnoty uloženy v seřazeném pořadí od nejmenšího po největší?
my_string = 1,9,5
print(my_string)

#Používá se pro přístup k hodnotám index?(Index je systémem vygenerované číslo 0,1,2.. )
my_string = "hello"
print(my_string[1])  # Výstup: e

#Je možné uložit dva stejné prvky?
my_string = "hello"
print(my_string)  # Výstup: hello (obsahuje dvě 'l')

#Je možné vložit hodnotu None?
my_nonestring = None
print(my_nonestring)

#Je možné kolekce vnořovat, tedy vložit jako prvek kolekce další kolekci s několika prvky?
my_set = {5,9}
mystring = my_set, "lopata"
print(mystring)
# Jakým způsobem zjistím počet prvků v kolekci?
my_string = "hello"
print(len(my_string))  # Výstup: 5

#Jakými všemi metodami je možné ověřit, jestli kolekce obsahuje nějaký prvek?
print('e' in my_string)  # Výstup: True

#Jakymi všemi metodami je možné získat hodnotu v pořadí třetího prvku v kolekci
my_string = "hello"
third_char = my_string[2]  # Získá třetí prvek (index 2)
print(third_char)  # Výstup: 'l'

