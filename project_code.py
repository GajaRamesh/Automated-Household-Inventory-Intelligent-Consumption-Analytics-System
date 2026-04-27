import json
import os

FILE_NAME = "inventory_data.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file)

def add_item(data):
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))

    data[name] = quantity
    save_data(data)

    print("Item added successfully!")

def view_inventory(data):
    print("\n--- Inventory ---")
    if not data:
        print("No items found.")
    else:
        for item, quantity in data.items():
            print(f"{item} -> Quantity: {quantity}")

def menu():
    data = load_data()

    while True:
        print("\n===== HI-CAS MENU =====")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item(data)
        elif choice == "2":
            view_inventory(data)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
