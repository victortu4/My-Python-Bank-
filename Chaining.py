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

User1 = User("Vic", "vic@mlb.com")
User2 = User("Jon", "jon@mlb.com")
User3 = User("Guido", "nick@mlb.com")



User1.deposit(100).deposit(40).deposit(170).withdraw(50)

User2.deposit(60).deposit(90).deposit(170).withdraw(70)

User3.deposit(70).deposit(120).deposit(110).withdraw(30)


User1.transfer(10, User3)
User2.transfer(15, User1)

User1.displayBalance()
User2.displayBalance()
User3.displayBalance()

