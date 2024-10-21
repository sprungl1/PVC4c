# Definice uzlu seznamu
class Node:
    def __init__(self, data):
        self.data = data  # Hodnota uzlu
        self.next = None  # Odkaz na další uzel

# Definice jednosměrného spojového seznamu
class LinkedList:
    def __init__(self):
        self.head = None  # Hlava seznamu je na začátku prázdná

    # Funkce pro přidání nového uzlu na konec seznamu
    def append(self, data):
        new_node = Node(data)  # Vytvoření nového uzlu
        if self.head is None:  # Pokud je seznam prázdný
            self.head = new_node  # Nový uzel se stává hlavou seznamu
            return
        last = self.head
        while last.next:  # Hledání posledního uzlu
            last = last.next
        last.next = new_node  # Připojení nového uzlu na konec seznamu

    # Funkce pro výpis všech prvků seznamu
    def print_list(self):
        current = self.head
        while current:  # Procházení seznamu, dokud neexistují další uzly
            print(current.data)
            current = current.next  # Posun na další uzel

# Vytvoření a naplnění spojového seznamu
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

# Výpis všech prvků seznamu
ll.print_list()
