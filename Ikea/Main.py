# TestIkeaItems.py
from Lack import Lack
from SamlaBox import SamlaBox
from Sjorraport import Sjorraport

# Create an instance of LACK
lack_item = Lack(shelf_number=1, aisle_letter='A', name='LACK Table', price=19.99, color='Black', height=45, width=55, length=55)
print(f"LACK Item: {lack_item.name}, Color: {lack_item.color}, Dimensions: {lack_item.height}x{lack_item.width}x{lack_item.length}")

# Manipulate LACK attributes
lack_item.color = 'White'
print(f"Updated LACK Color: {lack_item.color}")

# Create an instance of SAMLA_BOX
samla_box_item = SamlaBox(shelf_number=2, aisle_letter='B', name='SAMLA Box', price=5.99, volume=45, height=30, width=40, length=50, plastic_weight=200)
print(f"SAMLA BOX Item: {samla_box_item.name}, Volume: {samla_box_item.volume}L, Plastic Weight: {samla_box_item.plastic_weight}g, Dimensions: {samla_box_item.height}x{samla_box_item.width}x{samla_box_item.length}")

# Manipulate SAMLA_BOX attributes
samla_box_item.volume = 50
print(f"Updated SAMLA BOX Volume: {samla_box_item.volume}L")

# Create an instance of Sjorraport
sjorraport_item = Sjorraport(shelf_number=3, aisle_letter='C', name='SJÖRAPPORT Fish', price=9.99, expiration='2024-12-31', weight=500, plastic_weight=50)
print(f"SJÖRAPPORT Item: {sjorraport_item.name}, Expiration: {sjorraport_item.expiration}, Weight: {sjorraport_item.weight}g, Plastic Weight: {sjorraport_item.plastic_weight}g")

# Manipulate SJÖRAPPORT attributes
sjorraport_item.weight = 550
print(f"Updated SJÖRAPPORT Weight: {sjorraport_item.weight}g")