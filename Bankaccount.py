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


Checking.deposit(40).deposit(500).deposit(10).withdraw(2000).display_account_info()
Savings.deposit(500).deposit(300).withdraw(50).withdraw(60).withdraw(40).withdraw(100).yeild_interest().display_account_info()

# Checking.deposit(40)
# Checking.display_account_info()
# Checking.deposit(500)
# Checking.display_account_info()
# Checking.deposit(10)
# Checking.display_account_info()
# Checking.withdraw(2000)
# Checking.display_account_info()
# Checking.yeild_interest()
# Checking.display_account_info()



# Savings.deposit(500)
# Savings.deposit(300)
# Savings.withdraw(50)
# Savings.withdraw(60)
# Savings.withdraw(40)
# Savings.withdraw(100)
# Savings.yeild_interest()
# Savings.display_account_info()