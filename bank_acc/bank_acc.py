class BankAccount:
    def __init__(self,first_name,last_name,middle_name,account_type):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.account_type = account_type
        self.balance = 0.0
        self.status = "closed"

    def open_account(self):
        if self.status == "open":
            print("account already open")
        elif self.balance >= 100:
            self.status = "open"
            print("opening account")
        elif self.balance < 100:
            print("insufficient funds to open")
        else:
            print("general error: open_account")
    def overdraft_check(self):
        overdraft_fee = 35
        if self.balance < 0:
            self.balance -= overdraft_fee
        print(f"overdraft: ${overdraft_fee} has been deducted from your account")

    def deposit(self,ammount_to_deposit):
            self.balance += ammount_to_deposit
            print(f"depositing: ${ammount_to_deposit}, to {self.first_name} {self.account_type}:")
            self.display_balance()

    def withdraw(self, ammount_to_withdraw):
        if self.status == "open" or self.status == "closed":
            self.balance -= ammount_to_withdraw
            print(f"withdrawing: ${ammount_to_withdraw}")
            self.overdraft_check()
            self.display_balance()
        else:
            print("Your account may be frozen")

    def transfer(self, other_account, transfer_ammount):
        if self.status == "open" and other_account.status != "freeze":
            self.balance -= transfer_ammount
            other_account.balance += transfer_ammount
            print(f"${transfer_ammount} transfered to: {other_account.first_name}. ")
            self.overdraft_check()
        else:
            print("general error: transfer")

    def display_balance(self):
        print(f"current balance is : ${self.balance}")


#test cases for required functionality
acc1 = BankAccount('wade','welch','moneybags','savings')
acc2 = BankAccount('wade','welch','moneybags','checking')

#should be insufficient
acc1.open_account()
#add the money
acc1.deposit(1000)
#should open
acc1.open_account()
#should report already open
acc1.open_account()

acc2.open_account()
acc2.deposit(100)
acc2.open_account()

#should trasfer normaly
acc2.transfer(acc1,500)

#current parameters 100 - 500 should result in overdraft final balance -435
acc2.display_balance()

acc2.withdraw(500)
#current parameters -435-500 should overdraft again final balance -970
acc2.display_balance()
