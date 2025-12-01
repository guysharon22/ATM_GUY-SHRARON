
import datetime

customers = [
    {"name": "Avi Cohen", "pin": "1234", "balance": 1000},
    {"name": "Yossi Cohen", "pin": "6543", "balance": 500},
    {"name": "Yuri Levi", "pin": "5852", "balance": 800}
]

def find_customer(name):
    for customer in customers:
        if customer["name"].lower() == name.lower():
            return customer
    return None

def is_valid_amount(amount):
    return amount % 20 == 0 or amount % 50 == 0 or amount % 100 == 0

def atm_menu():
    print("\nATM MENU:")
    print("Press d to Deposit Money")
    print("Press w to Withdraw Money")
    print("Press c to Check your Balance")
    print("Press q to Quit")

def deposit(customer):
    try:
        amount = int(input("How much would you like to deposit? "))
        if is_valid_amount(amount):
            customer["balance"] += amount
            print("Deposit successful.")
        else:
            print("Invalid amount. You can only deposit multiples of 20, 50, or 100.")
    except ValueError:
        print("Please enter a valid number.")

def withdraw(customer):
    print("Choose amount to withdraw:")
    print("1 - 50\n2 - 100\n3 - 150\n4 - 300\n5 - Other amount")
    choice = input("Your choice: ")
    if choice in ["1", "2", "3", "4"]:
        amounts = {"1": 50, "2": 100, "3": 150, "4": 300}
        amount = amounts[choice]
    elif choice == "5":
        try:
            amount = int(input("Enter amount: "))
        except ValueError:
            print("Please enter a valid number.")
            return
    else:
        print("Invalid choice.")
        return

    if amount > customer["balance"]:
        print("Insufficient balance for this withdrawal.")
    elif not is_valid_amount(amount):
        print("Invalid amount. You can only withdraw multiples of 20, 50, or 100.")
    else:
        customer["balance"] -= amount
        print("Withdrawal successful.")

def check_balance(customer):
    print(f"Your current balance is: {customer['balance']} NIS")

def change_pin(customer):
    new_pin = input("Enter new PIN (4 digits): ")
    if len(new_pin) == 4 and new_pin.isdigit():
        customer["pin"] = new_pin
        print("PIN changed successfully.")
    else:
        print("Invalid PIN.")

def print_recipe(customer):
    now = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
    print(f"\nHello {customer['name']},")
    print(f"As of {now}, you have {customer['balance']} NIS in your account.")
    print("Thank you for using the ATM!\n")

def main():
    name = input("Enter your full name: ")
    customer = find_customer(name)
    if not customer:
        print("Customer not found.")
        return

    print(f"Welcome {customer['name']}!")
    pin = input("Enter your PIN (4 digits): ")
    if pin != customer["pin"]:
        print("Incorrect PIN.")
        return

    while True:
        atm_menu()
        choice = input("Your choice: ").lower()
        if choice == "d":
            deposit(customer)
        elif choice == "w":
            withdraw(customer)
        elif choice == "c":
            check_balance(customer)
        elif choice == "p":
            change_pin(customer)
        elif choice == "r":
            print_recipe(customer)
        elif choice == "q":
            print("WELCOME")
            break
        else:
            print("Invalid choice.")

# Start the program and allow multiple customers one after ayonother
while True:
    main()
