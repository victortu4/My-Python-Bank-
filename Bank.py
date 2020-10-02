class User:
    def __init__(self, nameInput, emailInput):
        self.name = nameInput
        self.email= emailInput
        self.account_balance = 0

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        if self.account_balance < amount:
            print("You overdrafted, charging $5 penalty fee")
            self.account_balance.balance -= 5
        else:
            self.account_balance -= amount
        return self

    def transfer(self, amount, receive):
        self.account_balance -= amount
        receive.account_balance += amount
        return self

    def displayBalance(self):
        print (f"{self.name} is ${self.account_balance}")
        return self


class BankAccount:
    def __init__(self, int_rate, balance):
        self.interest_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance>0:
            # self.balance+=self.balance*self.interest_rate
            self.balance = self.balance + (self.interest_rate * self.balance)
        return self

checking = BankAccount(0.05, 100)
savings = BankAccount (0.10, 1200)

print(checking)
print(savings)

checking.deposit(100).deposit(200).deposit(25).withdraw(75)
savings.deposit(200).deposit(600).withdraw(120).withdraw(43).withdraw(20).withdraw(140)

checking.yield_interest().display_account_info()
savings.yield_interest().display_account_info()




# User1.deposit(100).deposit(40).deposit(170).withdraw(50)

# User2.deposit(60).deposit(90).deposit(170).withdraw(70)

# User3.deposit(70).deposit(120).deposit(110).withdraw(30)


# # User1.transfer(10, User3)
# # User2.transfer(15, User1)

# User1.displayBalance()
# User2.displayBalance()
# User3.displayBalance()