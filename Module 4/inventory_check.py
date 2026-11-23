"""
Project Name: Destiny Survival Inventory
Created By: Natasha Evelyn
Description: A program to manage the Guardian's inventory before going out to battle.
"""

#! Global inventory dictionary
guardian_inventory = {
    "Ghosts": 3,
    "Gauntlets": 9,
    "Power Weapons": 6,
    "Ships": 3,
    "Sparrows": 4
}

#! Function to view the inventory
def view_inventory():
    print("\n Current Guardian Inventory: ")

    for item, quantity in guardian_inventory.items():
        print(f"{item}: {quantity}")

    return guardian_inventory

#! Function to add items to the inventory
def add_item(item_name, quantity):

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero!")

    if item_name in guardian_inventory:
        guardian_inventory[item_name] += quantity
    else:
        guardian_inventory[item_name] = quantity

    return guardian_inventory


#! Function to remove items from the inventory
def remove_item(item_name, quantity):

    if item_name not in guardian_inventory:
        raise KeyError(f"{item_name} is not in the current inventory.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero, traveler!")

    if guardian_inventory[item_name] < quantity:
        raise ValueError(f"Not enough {item_name} to remove!")

    guardian_inventory[item_name] -= quantity

    if guardian_inventory[item_name] == 0:
        del guardian_inventory[item_name]

    return guardian_inventory

#! Main program
try:
    print("🌙 Welcome to the Guardian Maintenance Manager. We are here to make sure you protect The Last City. Verify your inventory before leaving.")

    #? Display initial inventory
    view_inventory()

    #? Add new items
    print("\n✨ Adding 7 Silken Codex...")
    add_item("Silken Codex", 7)
    view_inventory()

    #! Remove existing items
    print("\n✨ Removing 1 Sparrow...")
    remove_item("Sparrows", 1)
    view_inventory()

    #! Attempt to remove too many items
    print("\nAttempting to retrieve 12 Power Weapons...")
    remove_item("Power Weapons", 12)

except KeyError as key_e:
    print(f"\n Error: {key_e}")

except ValueError as val_e:
    print(f"\n Error: {val_e}")

else:
    print("\n All inventory operations completed successfully.")

finally:
    print("\n Guardian inventory management complete. You may depart.")

    print("\nFinal Inventory:")
    view_inventory()
