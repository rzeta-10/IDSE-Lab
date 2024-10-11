#CS22B1093 ROHAN G

import datetime

class Account:
    def __init__(self, name, acc_no, acc_type):
        self.name = name
        self.acc_no = acc_no
        self.acc_type = acc_type

class SavingsAccount(Account):
    def __init__(self, name, acc_no, balance):
        super().__init__(name, acc_no, 'Savings')
        self.__balance = balance
    
    def withdraw(self, amount):
        if self.__balance - amount < 0:
            print(f"Insufficient balance. Current balance is {self.__balance}. Withdrawal not allowed.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")
    
    def show_balance(self):
        print(f"Balance: {self.__balance}")

class CurrentAccount(Account):
    def __init__(self, name, acc_no):
        super().__init__(name, acc_no, 'Current')
        print(f"Current account successfully created for {self.name}, Account No: {self.acc_no}")

def generate_account_number():
    return datetime.datetime.now()

while True:
    print(f"Choose which account do you want to create:")
    print(f"1. Savings")
    print(f"2. Current")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter your name: ")
        acc_no = generate_account_number()
        balance = float(input("Enter initial balance: "))
        s_acc = SavingsAccount(name, acc_no, balance)
        s_acc.show_balance()
        s_acc.withdraw(200)
        s_acc.deposit(100)  
        s_acc.show_balance()
        
    elif choice == 2:
        name = input("Enter your name: ")
        acc_no = generate_account_number()
        c_acc = CurrentAccount(name, acc_no)
        
    else:
        print("Invalid choice. Please select 1 or 2.")
    
    another = input("Do you want to create another account? (yes/no): ").lower()
    if another != 'yes':
        break
