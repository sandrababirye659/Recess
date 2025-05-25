# Create an inventory management system - Use loops to display or update a list of stock items
from random import choices

inventory ={
    "Apples": 50,
    "Bananas": 30,
    "Oranges": 20
}
while True:
    print("\n Inventory Management System")
    print("1.View Inventory")
    print("2.Update Inventory")
    print("3.Exit")

    choice = input("Enter your choice (1-3)")
    if choice =='1':
        print("\nCurrent inventory:")
        for item, quantity  in inventory.items():
            print(f"{item}:{quantity}")
    elif choice == '2':
        item = input("Enter the item name to update/add:").capitalize()
        try:
            quantity = int(input("Enter the quantity to add (Use negative numbers to subtract)"))
            if item in inventory:
                inventory[item]+= quantity

            else:
                inventory[item] = quantity

                print(f"Updated {item}:{inventory[item]}")
        except ValueError:
            print("Invalid quantity.Please enter a number")
    elif choice == '3':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice.Please choose from 1-3.")
