import re
from math import sqrt


lipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam cursus convallis magna, et hendrerit arcu ornare et."

sentences = len(re.findall(r'\w+', lipsum))

print("Wordcount: {}\n".format(sentences))

print("sqrt(100) = {}\nsqrt(2) = {}\n".format(sqrt(100), sqrt(2)))

# from https://wiki.python.org/moin/SimplePrograms
class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def overdrawn(self):
        return self.balance < 0
my_account = BankAccount(15)
my_account.withdraw(50)
print (my_account.balance, my_account.overdrawn())