class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DequeQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        """Přidání prvku na konec fronty"""
        new_node = Node(data)
        if self.tail is None:  # fronta je prázdná
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def pop(self):
        """Získání a odstranění prvku ze začátku fronty"""
        if self.head is None:
            raise IndexError("pop() called on an empty queue")

        data = self.head.data
        if self.head == self.tail:  # ve frontě je jen jeden prvek
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return data

    def count(self):
        """Získání počtu prvků ve frontě"""
        return self.size

    def clear(self):
        """Vyprázdnění celé fronty"""
        self.head = self.tail = None
        self.size = 0

    def popAll(self):
        """Získání všech prvků a vyprázdnění fronty"""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        self.clear()
        return tuple(elements)  # nebo return list(elements), pokud chcete list


# Testování
queue = DequeQueue()
queue.add(1)
queue.add(2)
queue.add(3)
print(queue.pop())  # Výstup: 1
print(queue.count())  # Výstup: 2
print(queue.popAll())  # Výstup: (2, 3)
print(queue.count())  # Výstup: 0
