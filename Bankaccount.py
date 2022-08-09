

class BankAccount:
    bank_balance = 0
    bank_interest = 0.01

    
    def __init__(self, init_rate, balance):
        self.init_rate = init_rate
        self.balance  = balance

    def deposit(self, amount):
        self.balance = self.balance + (amount)
        return self

    def withdraw(self,amount):
        self.balance = self.balance - (amount)
        if self.balance <= 0:
                self.balance = self.balance + (amount) - 5
                print('Insufficient funds: Charging a %5 fee')
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yeild_interest(self):
        if self.balance <= 0:
            return
        self.balance = self.balance + (self.balance * BankAccount.bank_interest)
        return self


Checking = BankAccount(BankAccount.bank_interest, 800)
Savings = BankAccount(BankAccount.bank_interest, 300)

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(init_rate=0.02, balance=0)

    def make_deposit(self):
        self.account.deposit(100)
        print(self.account.balance)
        return

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return
    
    def display_user_balance(self):
        self.account.display_account_info
        return

