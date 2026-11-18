# Global inventory dictionary
inventory = {
    "Green Shell": 3,
    "Banana": 5,
    "Mushroom": 2
}

# Function to view the inventory
def view_inventory():
    print("\nCurrent Inventory:") # whats that \n mean again?
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")
    return inventory

# Function to add items to the inventory
def add_item(item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    return inventory

# Function to remove items from the inventory
def remove_item(item_name, quantity):
    if item_name not in inventory:
        raise KeyError(f"{item_name} is not in the inventory!")
    if inventory[item_name] < quantity:
        raise ValueError(f"Not enough {item_name} to remove!")
    inventory[item_name] -= quantity
    if inventory[item_name] == 0:
        del inventory[item_name]
    return inventory

# Main program to test the functions
try:
    print("Welcome to Mario Kart Inventory Manager!")
    view_inventory()

    # Adding items
    print("\nAdding 2 Red Shells...")
    add_item("Red Shell", 2)
    view_inventory()

    # Removing items
    print("\nRemoving 3 Bananas...")
    remove_item("Banana", 3)
    view_inventory()

    # Attempting to remove too many items
    print("\nAttempting to remove 10 Green Shells...")
    remove_item("Green Shell", 10)

except KeyError as key_e:
    print(f"Error: {key_e}")
except ValueError as val_e:
    print(f"Error: {val_e}")
finally:
    print("\nInventory management complete!")

    # All of this is the example to follow. We must make our own