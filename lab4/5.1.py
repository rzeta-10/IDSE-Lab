# Global counter for total items sold
total_count = 0

class ZZYO:
    # Constructor to initialize the object with the given item details
    def __init__(self, item_no, item_name, price, discount=0, count=0, number_sold=0):
        self.item_no = item_no
        self.item_name = item_name
        self.price = price
        self.discount = discount
        self.count = count
        self.number_sold = number_sold
    
    # Method to handle buying of an item
    def item_buy(self):
        global total_count
        
        if self.count > 0:
            total_count += 1
            self.count -= 1
            self.number_sold += 1
            print(f"Item {self.item_name} bought successfully!")
        else:
            print(f"Item {self.item_name} is out of stock!")

        # Apply discount every 5 sales
        if self.number_sold % 5 == 0:
            print(f"Congratulations! You've earned a discount of {self.discount}% on {self.item_name}!")

    # Method to increment discount if there have been no sales
    def apply_discount(self):
        if self.number_sold == 0 and self.discount < 50:
            self.discount += 5
            print(f"No sales for {self.item_name}. Discount increased to {self.discount}%.")
        elif self.discount >= 50:
            print(f"Discount for {self.item_name} has reached the maximum of 50%.")
    
    # Display item details
    def display(self):
        print(f"Item No: {self.item_no}, Name: {self.item_name}, Price: {self.price}, "
              f"Discount: {self.discount}%, Count: {self.count}, Sold: {self.number_sold}")


# Inventory list to store all items
inventory = []

# Function to add item to inventory
def add_item():
    item_no = int(input("Enter the item number: "))
    item_name = input("Enter the item name: ")
    price = float(input(f"Enter the price of {item_name}: "))
    discount = float(input(f"Enter the discount for {item_name}: "))
    count = int(input(f"Enter the count of {item_name}: "))
    
    item = ZZYO(item_no, item_name, price, discount, count)
    inventory.append(item)
    print(f"Item {item_name} added successfully to the inventory!")

# Function to remove an item from the inventory
def remove_item():
    item_no = int(input("Enter the item number to remove: "))
    for item in inventory:
        if item.item_no == item_no:
            inventory.remove(item)
            print(f"Item {item.item_name} removed from the inventory.")
            return
    print(f"Item with number {item_no} not found.")

# Function to buy an item
def buy_item():
    item_no = int(input("Enter the item number to buy: "))
    for item in inventory:
        if item.item_no == item_no:
            item.item_buy()
            return
    print(f"Item with number {item_no} not found.")

# Function to display the current inventory
def display_inventory():
    print("\nCurrent Inventory:")
    for item in inventory:
        item.display()
    print()

# Menu-driven program
def menu():
    while True:
        print("\nChoose one of the following options:")
        print("1. Set Inventory")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Buy Item")
        print("5. Display Inventory")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_item()
        elif choice == 2:
            add_item()
        elif choice == 3:
            remove_item()
        elif choice == 4:
            buy_item()
        elif choice == 5:
            display_inventory()
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the menu
menu()
