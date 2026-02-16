class ATM:
    def __init__(self):
        self.balance = 1000

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

class ATM2:
    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New Balance: {self.balance}")

class ATM3(ATM2, ATM):  # multiple inheritance: derives from ATM2 and ATM
    def menu(self):
        while True:
            print("\nATM Menu:\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                self.deposit()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                print(f"Current Balance: {self.balance}")
            elif choice == '4':
                print("Thank you for using ATM!")
                break
            else:
                print("Invalid option.")

# Create object of derived class ATM3 and run menu
atm = ATM3()
atm.menu()



# Exmple2

class Deposit:
    def deposit(self, balance):
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Deposited: {amount}. New Balance: {balance}")
        else:
            print("Deposit amount must be positive.")
        return balance

class Withdraw:
    def withdraw(self, balance):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            print(f"Withdrawn: {amount}. New Balance: {balance}")
        return balance

class ATM(Deposit, Withdraw):
    def __init__(self):
        self.balance = 1000

    def menu(self):
        while True:
            print("\nATM Menu:\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                self.balance = self.deposit(self.balance)
            elif choice == '2':
                self.balance = self.withdraw(self.balance)
            elif choice == '3':
                print(f"Current Balance: {self.balance}")
            elif choice == '4':
                print("Thank you for using ATM!")
                break
            else:
                print("Invalid option.")


atm = ATM()
atm.menu()
