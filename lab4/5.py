#CS22B1093 ROHAN G

total_count = 0

class ZZYO:
    def __init__(self,item_no,item_name,price,discount,count,number_sold):
        self.item_no = item_no
        self.item_name = item_name
        self.price = price
        self.discount = discount
        self.count = count
        self.number_sold = number_sold
    
    def item_buy(self):
        global total_count
        if self.count == 0:
            print(f"Item {self.item_name} is out of stock !!")
            return
        else:
            total_count += 1
            self.count -= 1
            self.number_sold += 1
            print(f"Item {self.item_name} bought successfully !!")

        if self.number_sold == 0 and self.discount < 50:
            self.discount += 5
            print(f"No items sold yet !! Discount increased by 5% !!")
        elif self.discount >= 50:
            print(f"Item {self.item_name} has reached maximum discount !!")
            return
        elif self.number_sold%5 == 0:
            self.discount += 5
            print(f"Item {self.item_name} has reached 5 items sold !! Discount increased by 5% !!")

inventory = []

while True:
    print(f"Choose one of the following options : ")
    print(f"1.Set Inventory\n2.Add Item\n3.Remove Item\n4.Buy Item\n5.Display Inventory\n6.Exit")
    choice = int(input())

    if(choice == 1):
        item_no = int(input("Enter the item number : "))
        item_name = input("Enter the item name : ")
        price = float(input("Enter the price of the item : "))
        discount = float(input("Enter the discount on the item : "))
        count = int(input("Enter the count of the item : "))
        # number_sold = int(input("Enter the number of items sold : "))
        item = ZZYO(item_no,item_name,price,discount,count,0)
        inventory.append(item)
        print(f"Item {item_name} successfully added to inventory set!!")
    
    elif(choice == 2):
        item_no = int(input("Enter the item number to be added : "))
        for item in inventory:
            if item.item_no == item_no:
                increase_count = int(input("Enter the count to be added : "))
                item.count += increase_count
                print(f"Item {item.item_name} count increased successfully !!")
                break
        else:
            print(f"Item not found in inventory !!")
    elif(choice == 3):
        item_no = int(input("Enter the item number to be removed : "))
        for item in inventory:
            if item.item_no == item_no:
                decrease_count = int(input("Enter the count to be removed : "))
                item.count -= decrease_count
                print(f"Item {item.item_name} count decreased successfully !!")
                break
        else:
            print(f"Item not found in inventory !!")
    elif(choice == 4):
        item_no = int(input("Enter the item number to be bought : "))
        for item in inventory:
            if item.item_no == item_no:
                item.item_buy()
                print(f"Item {item.item_name} bought successfully !!")
                break
        else:
            print(f"Item not found in inventory !!")
    
    elif(choice == 5):
        for item in inventory:
            print(f"Item Number : {item.item_no}")
            print(f"Item Name : {item.item_name}")
            print(f"Price : {item.price}")
            print(f"Discount : {item.discount}")
            print(f"Count : {item.count}")
            print(f"Number Sold : {item.number_sold}")
            print(f"-----------------------------------")

        print(f"Total items bought : {total_count}")     
    elif(choice == 6):
        print(f"Exiting the program !!")
        break

    else:
        print(f"Invalid choice !! Please choose a valid option !!")
        continue
