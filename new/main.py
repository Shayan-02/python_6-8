# Define a class called Bank to implement a simple banking system
class Bank:
    # Initialize the bank with an empty dictionary to store customer accounts and balances
    def __init__(self):
        self.customers = {}

    # Create a new account with a given account number and an optional initial balance (default to 0)
    def create_account(self, account_number, initial_balance=0):
        if account_number in self.customers:
            print("Account number already exists.")
        else:
            self.customers[account_number] = initial_balance
            print("Account created successfully.")

    # Make a deposit to the account with the given account number
    def make_deposit(self, account_number, amount):
        if account_number in self.customers:
            self.customers[account_number] += amount
            print("Deposit successful.")
        else:
            print("Account number does not exist.")

    # Make a withdrawal from the account with the given account number
    def make_withdrawal(self, account_number, amount):
        if account_number in self.customers:
            if self.customers[account_number] >= amount:
                self.customers[account_number] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Account number does not exist.")

    # Check and print the balance of the account with the given account number
    def check_balance(self, account_number):
        if account_number in self.customers:
            balance = self.customers[account_number]
            print(f"Account balance: {balance}")
        else:
            print("Account number does not exist.")

# Example usage
# Create an instance of the Bank class
bank = Bank()

# Create customer accounts and perform account operations
acno1= "SB-123"
damt1 = 1000
print("New a/c No.: ",acno1,"Deposit Amount:",damt1)
bank.create_account(acno1, damt1)

acno2= "SB-124"
damt2 = 1500
print("New a/c No.: ",acno2,"Deposit Amount:",damt2)
bank.create_account(acno2, damt2)

wamt1 = 600
print("\nDeposit Rs.",wamt1,"to A/c No.",acno1)
bank.make_deposit(acno1, wamt1)

wamt2 = 350
print("Withdraw Rs.",wamt2,"From A/c No.",acno2)
bank.make_withdrawal(acno2, wamt2)

print("A/c. No.",acno1)
bank.check_balance(acno1)

print("A/c. No.",acno2)
bank.check_balance(acno2)

wamt3 = 1200
print("Withdraw Rs.",wamt3,"From A/c No.",acno2)
bank.make_withdrawal(acno2, wamt3)

acno3 = "SB-134"
print("A/c. No.",acno3)
bank.check_balance(acno3)  # Non-existent account number 
