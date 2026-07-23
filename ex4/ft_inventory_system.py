import sys

inventory = {}
errors = []
for arg in sys.argv[1:]:
    if ':' not in arg:
        errors.append(f"Error - invalid parameter '{arg}'")
        continue

    parts = arg.split(':', 1)
    item_name = parts[0]
    qty_str = parts[1]
    if item_name in inventory:
        errors.append(f"Redundant item '{item_name}' - discarding")
        continue
    try:
        qty = int(qty_str)
    except ValueError:
        errors.append(f"Quantity error for '{item_name}': invalid literal for int() with base 10: '{qty_str}'")
        continue
    inventory[item_name] = qty
print("=== Inventory System Analysis ===")
for error in errors:
    print(error)

print(f"Got inventory: {inventory}")
print(f"Item list: {list(inventory.keys())}")

# Calcul du total
total = sum(inventory.values())
print(f"Total quantity of the {len(inventory)} items: {total}")
for item in inventory.keys():
    qty = inventory[item]
    percent = round((qty / total) * 100, 1)
    print(f"Item {item} represents {percent}%")
most_item = ""
most_qty = -1
least_item = ""
least_qty = sum(inventory.values()) + 1
for item in inventory.keys():
    qty = inventory[item]
    if qty > most_qty:
        most_qty = qty
        most_item = item
    if qty < least_qty:
        least_qty = qty
        least_item = item

print(f"Item most abundant: {most_item} with quantity {most_qty}")
print(f"Item least abundant: {least_item} with quantity {least_qty}")
inventory.update({"magic_item": 1})
print(f"Updated inventory: {inventory}")