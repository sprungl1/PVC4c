class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    # Vložení nového prvku na vrchol zásobníku
    def add(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    # Získání a smazání vrcholu zásobníku
    def pop(self):
        if self.top is None:
            raise IndexError("pop from an empty stack")
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    # Získání počtu prvků v zásobníku
    def count(self):
        return self.size

    # Vypráznění celého zásobníku
    def clear(self):
        self.top = None
        self.size = 0

    # Vrácení všech prvků v zásobníku jako list (a jeho vyprázdnění)
    def popAll(self):
        elements = []
        while self.top is not None:
            elements.append(self.pop())
        return elements

# Testování zásobníku
stack = Stack()

# Přidání prvků
stack.add(10)
stack.add(20)
stack.add(30)

# Výpis počtu prvků
print(f"Počet prvků: {stack.count()}")  # Očekávaný výstup: 3

# Odebrání vrcholu zásobníku
print(f"Vrchol: {stack.pop()}")  # Očekávaný výstup: 30

# Výpis počtu po odebrání
print(f"Počet prvků po odebrání: {stack.count()}")  # Očekávaný výstup: 2

# Vyprázdnění zásobníku a výpis všech prvků
print(f"Všechny prvky: {stack.popAll()}")  # Očekávaný výstup: [20, 10]

# Zkusíme pop na prázdný zásobník
try:
    stack.pop()
except IndexError as e:
    print(f"Chyba: {e}")  # Očekávaná chyba: pop from an empty stack

# Vymazání zásobníku
stack.clear()
print(f"Počet prvků po vyčištění: {stack.count()}")  # Očekávaný výstup: 0
