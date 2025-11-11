# bam
'''
print("         ______")
print("        /      \\ ")
print("       | \\_  _/ |")
print("      (| @ ]  @ |)")
print("        \\  __  /")
print(" ____   |\\____/|   ____")
print("/    \\_/        \\_/    \\")
print("")
'''

# Write a class for a bank account. A bank account should have an owner and a balance and should be able to:
# Deposit money
# withdraw money

# dictionary?

class BankAccount:
    rate = 0.02
    def __init__(self, name, initial_balance = 0):
        self.balance = initial_balance
        self.owner = name
    def deposit(self,value):
        self.balance += value
    def withdraw(self,value):
        if value > self.balance:
            print("Insufficient funds")
        else:
            print(f"Here is your ${value}.")
            self.balance -= value
    def get_balance(self):
        return self.balance
    def get_owner(self):
        return self.owner
    def set_owner(self,new_owner):
        self.owner = new_owner
    def __str__(self):
        return f"Owner: {self.get_owner()}; balance: ${self.get_balance()}"
    # The following method LOOKS like it operates correctly, but the new balance, $900, 
    # is returned as a string when we want an integer.
    def __add__(self,other):
        new_owner = f"{self.get_owner()} & {other.get_owner()}"
        new_balance = self.get_balance() + other.get_balance()
        #new_account = f"Owner: {new_owner}, balance: ${new_balance}"
        # we are going to create a new account which isof type bank account,
        #  then add in a constructor that takes a name and initial balance.
        new_account = BankAccount(new_owner,new_balance)
        return new_account
    def __eq__(self, other):
        return self.get_owner() == other.get_owner() 
    def give_interest(self):
        # This should add some amount of interest to the balance.
        self.balance = self.balance + self.balance * self.rate



matt_acc = BankAccount("Matt")
ashley_acc = BankAccount("Ashley",500)
print(ashley_acc)
ashley_acc.give_interest()
print(ashley_acc)

print(ashley_acc.rate)
print(matt_acc.rate)
matt_acc.rate = .03
print(matt_acc.rate)
print(ashley_acc.rate)




#shopping cart or playlist questions in classes 3 quiz list is good prep for CIS 122
# do it fr









