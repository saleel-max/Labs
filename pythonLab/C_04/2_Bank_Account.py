class BankAccount:
    def __init__(a, acc_number, name, acc_type, balance):
        a.acc_number = acc_number
        a.name = name
        a.acc_type = acc_type
        a.balance = balance

    def deposit(a, amount):
        if amount > 0:
            a.balance += amount
            print(f"Deposited {amount}. New balance: {a.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(a, amount):
        if amount > 0:
            if amount <= a.balance:
                a.balance -= amount
                print(f"Withdrew {amount}. New balance: {a.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

acc_number = input("Enter account number: ")
name = input("Enter account holder name: ")
acc_type = input("Enter account type: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(acc_number, name, acc_type, balance)

deposit_amount = float(input("Enter amount to deposit: "))
account.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount)
