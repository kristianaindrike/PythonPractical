#Create a class named BankAccount that has the following attributes: account_number, balance, and owner_name. 
#It should also have methods called deposit() and withdraw() that update the balance accordingly.

# class BankAccount:
#     def __init__(self,account_number,balance,owner_name) -> None:
#         self.account_number = account_number
#         self.balance = balance
#         self.owner_name = owner_name

#     def deposit(self,addmoney):
#         addmoney = str(input("Enter your deposit: "))
#         return "Balance: " + str(self.balance + addmoney)
#     def withdraw(self,removemonay):
#         self.removemoney = str(input("Enter your withdraw: "))
#         return "Balance: " + str(self.balance - removemoney)
    
# client1 = BankAccount(34,450,"Janis")
# print(client1.deposit(), client1.withdraw())

#Dataclass

from dataclasses import dataclass

@dataclass
class BankAccount:
    account_number:str
    balance:float
    owner_name:str

    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if amount > self.balance:
           print("Not possible to withdraw. because the amount exceeds your balance.")
        else:
           self.balance -= amount

bank_account = BankAccount("LV5674",450,"Janis")
print(bank_account)
bank_account.deposit(100)
print(bank_account)
bank_account.withdraw(400)
print(bank_account)