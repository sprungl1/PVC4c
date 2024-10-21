# Definice třídy pro uzel obousměrného spojového seznamu
class Node:
    def __init__(self, data):
        self.data = data  # Hodnota uzlu
        self.next = None  # Odkaz na další uzel
        self.prev = None  # Odkaz na předchozí uzel

# Definice třídy pro obousměrný spojový seznam
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Hlavní uzel (první uzel seznamu)

    # Metoda pro přidání uzlu na konec seznamu
    def append(self, data):
        new_node = Node(data)  # Vytvoření nového uzlu
        if self.head is None:
            # Pokud je seznam prázdný, nový uzel se stává hlavou
            self.head = new_node
        else:
            # Procházení seznamu na konec
            current = self.head
            while current.next:
                current = current.next
            # Přidání nového uzlu na konec
            current.next = new_node
            new_node.prev = current

    # Metoda pro výpis seznamu od prvního k poslednímu uzlu
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    # Metoda pro výpis seznamu od posledního k prvnímu uzlu
    def display_backward(self):
        current = self.head
        if not current:
            return
        # Procházení na konec seznamu
        while current.next:
            current = current.next
        # Výpis od posledního k prvnímu
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

# Vytvoření instance obousměrného spojového seznamu
dll = DoublyLinkedList()

# Přidání alespoň 5 prvků do seznamu
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)

# Výpis seznamu od prvního k poslednímu
print("Forward:")
dll.display_forward()

# Výpis seznamu od posledního k prvnímu
print("Backward:")
dll.display_backward()
