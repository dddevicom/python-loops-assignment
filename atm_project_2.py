class ATM ():
    def __init__(self, bank_name, location, serial):
        self.bank_name = bank_name
        self.location = location
        self.serial = 12345
        self.balance = 1000  # default starting balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")


# Create ATM object
sbin = ATM("SBI", "Hyderabad", 1234)

# Interactive menu loop
while True:
    print("\n===== ATM MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        sbin.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        sbin.withdraw(amount)
    elif choice == "3":
        sbin.check_balance()
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
