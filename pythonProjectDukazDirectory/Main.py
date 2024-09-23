# Je zachovano poradi ve kterem jsou prvky kolekce vkladany?
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict)  # Výstup: {'a': 1, 'b': 2, 'c': 3}

#Jsou hodnoty uloženy v seřazeném pořadí od nejmenšího po největší?
my_dict = {"c": 3, "a": 1, "b": 2}
print(my_dict)  # Výstup: {'c': 3, 'a': 1, 'b': 2}

#Používá se pro přístup k hodnotám index?
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict["b"])  # Výstup: 2

#Je možné uložit dva stejné prvky?
my_dict = {"a": 1, "b": 2, "a": 3}
print(my_dict)  # Výstup: {'a': 3, 'b': 2}

#Je možné vložit hodnotu None
my_dict = {"a": None, "b": 2}
print(my_dict)  # Výstup: {'a': None, 'b': 2}

#Je možné kolekce vnořovat, tedy vložit jako prvek kolekce další kolekci s několika prvky?\
myset = {6,8,6}
my_dict = {"a": myset, "b":7}
print(my_dict)  # Výstup:{'a': {8, 6}, 'b': 7}
#Je možné za běhu programu změnit velikost kolekce?
my_dict = {"a": 1, "b": 2}
my_dict["c"] = 3  # Přidání nového prvku
del my_dict["a"]  # Odebrání prvku
print(my_dict)  # Výstup: {'b': 2, 'c': 3}
#Jakým způsobem zjistím počet prvků v kolekci?
my_dict = {"a": 1, "b": 2}
print(len(my_dict))  # Výstup: 2

#Jakými všemi metodami je možné vložit nový prvek do kolekce a jaké mají tyto metody vstupy?
my_dict = {"a": 1}
my_dict["b"] = 2  # Přidání nového prvku
print(my_dict)  # Výstup: {'a': 1, 'b': 2}

#Jakými všemi metodami je možné smazat/odebrat existující prvek do kolekce a jaké mají tyto metody vstupy?
my_dict = {"a": 1, "b": 2}
del my_dict["a"]  # Smaže prvek s klíčem "a"
print(my_dict)  # Výstup: {'b': 2}

my_dict = {"a": 1, "b": 2}
my_dict.pop("b")  # Odebere a vrátí hodnotu pro klíč "b"
print(my_dict)  # Výstup: {'a': 1}

#Jakými všemi metodami je možné ověřit, jestli kolekce obsahuje nějaký prvek?
my_dict = {"a": 1, "b": 2}
if "a" in my_dict:
    print("Prvek s klíčem 'a' existuje")  # Výstup: Prvek s klíčem 'a' existuje
#Jakymi všemi metodami je možné upravit hodnotu existujícího prvek v kolekci a jaké mají tyto metody vstypy?
    my_dict = {"a": 1, "b": 2}
    my_dict.update({"a": 10})  # Změna hodnoty pro klíč "a"
    print(my_dict)  # Výstup: {'a': 10, 'b': 2}

#Jakými všemi metodami je možné získat hodnotu v pořadí třetího prvku v kolekci?
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
third_item = list(my_dict.items())[2]  # Získá třetí prvek jako pár (klíč, hodnota)
print(third_item)  # Výstup: ('c', 3)





