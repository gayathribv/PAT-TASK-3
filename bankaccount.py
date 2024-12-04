class BankAccount:


    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.__balance = balance
   
    def deposit(self, amount):
        """METHOD : For Deposit"""
        if amount > 0:
            self.__balance = self.__balance + amount
            return self.__balance
        else:
            return "ERROR : Invalid Amount Deposited !"
   
    def withdraw(self, amount):
        """METHOD : For Withdraw"""
        if 0 < amount <= self.__balance:
            self.__balance = self.__balance - amount
            return self.__balance
        else:
            return "ERROR : Insufficient Funds in the account !"
   
    def get_balance(self):
        """METHOD : Fetch the account Balance"""
        return self.__balance
   
    def set_balance(self, amount):
        """METHOD : Set the Balance"""
        if amount >= 0:
            self.__balance = amount
        else:
            return "ERROR : Invalid Balance Account"








class SavingsAccount(BankAccount):


    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
   
    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        return interest
   
    def apply_interest(self):
        interest = self.calculate_interest()
        self.deposit(interest)
        return self.get_balance()

class CurrentAccount(BankAccount):


    def __init__(self, account_number, balance=0, od_balance=0, Annual_interest_rate=0.11):
        super().__init__(account_number, balance)
        self.interest_rate = Annual_interest_rate
        self.od_balance=od_balance
   
    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        return interest
   
    def apply_interest(self):
        interest = self.calculate_interest()
        self.deposit(interest)
        return self.get_balance()
    
    def deposit(self, amount)
        if amount > 0 and od_balance == 0:
            self.balance = self.balance + amount
        else if amount > 0 and od_balance

if __name__ == "__main__":
    savings_account = SavingsAccount(account_number=9835, balance=5000, interest_rate=0.03)
    print(savings_account.deposit(1000))
    print(savings_account.withdraw(2000))
    print(savings_account.apply_interest())


