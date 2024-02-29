class bal_exp(Exception):
    pass

class bankacc:
    def __init__(self,initial_amt,acc_name):
        self.bal=initial_amt
        self.name=acc_name
        print(f"\naccount {self.name} created. \nbalance=${self.bal:.2f}")
    def get_bal(self):
        print(f"\naccount {self.name} balence=${self.bal:.2f}")

    def deposit(self,amount):
        self.bal=self.bal+amount
        print(f"\ndeposit complete")
        self.get_bal()
    def viabl_transaction(self,amount):
        if self.bal>=amount:
            return
        else:
            raise bal_exp(f"\nsorry, account {self.name} only has balence of ${self.bal:.2f}")
    def withdraw(self,amount):
        try:
            self.viabl_transaction(amount)
            self.bal=self.bal-amount
            print("\nwithdraw complete")
            self.get_bal()
        except bal_exp as error:
            print(f"\nwithdraw intrrupted: {error}")

    def transfer(self,amount,account):
        try:
            print("\n*********\n\nbeginning transfer.. 🚀")
            self.viabl_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\ntransfer complete..\n\n***********")
        except bal_exp as error:
            print(f"\ntransfer interrupted. ❌ {error}")

class interest_reward_acc(bankacc):
    def deposit(self,amount):
        self.bal=self.bal+(amount*1.05)
        print("\ndeposit complete.")
        self.get_bal()

class savings_acc(interest_reward_acc):
    def __init__(self,initial_amt,acc_name):
        super().__init__(initial_amt,acc_name)
        self.fee=5
    def withdraw(self,amount):
        try:
            self.viabl_transaction(amount+self.fee)
            self.bal=self.bal-(amount+self.fee)
            print("\nwithdraw completed.")
            self.get_bal()
        except bal_exp as error:
            print(f"\nwithdraw interrupted: {error}")