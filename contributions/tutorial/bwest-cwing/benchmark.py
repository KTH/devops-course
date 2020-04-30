# most code gathered from https://wiki.python.org/moin/SimplePrograms
import random
import re
from time import localtime
from math import sqrt, exp

class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def overdrawn(self):
        return self.balance < 0

def greet(name):
    a ='Hello'.format(name)

BOARD_SIZE = 3

def under_attack(col, queens):
    left = right = col

    for r, c in reversed(queens):
        left, right = left - 1, right + 1

        if c in (left, col, right):
            return True
    return False

def solve(n):
    if n == 0:
        return [[]]

    smaller_solutions = solve(n - 1)

    return [solution+[(n,i+1)]
        for i in range(BOARD_SIZE)
            for solution in smaller_solutions
                if not under_attack(i+1, solution)]
                
import itertools

def iter_primes():
     # an iterator of all numbers between 2 and +infinity
     numbers = itertools.count(2)

     # generate primes forever
     while True:
         # get the first number from the iterator (always a prime)
         prime = next(numbers)
         yield prime

         # this code iteratively builds up a chain of
         # filters...slightly tricky, but ponder it a bit
         numbers = filter(prime.__rmod__, numbers)
         



def tasks():
    lst = []
    for i in range(100):
        t = random.randint(0,100)
        lst.append(t)
        sqrt(t)
        exp(t)
        friends = ['john', 'pat', 'gary', 'michael']
        for i, name in enumerate(friends):
            a ="iteration {iteration} is {name}".format(iteration=i, name=name)
        parents, babies = (1, 1)
        while babies < 5:
            a ='This generation has {0} babies'.format(babies)
            parents, babies = (babies, parents + babies)
        greet('Jack')
        greet('Jill')
        greet('Bob')
        for test_string in ['555-1212', 'ILL-EGAL']:
            if re.match(r'^\d{3}-\d{4}$', test_string):
                a = '{0} is a valid US local phone number'.format(test_string)
            else:
                a = '{0} rejected'.format(test_string)
        prices = {'apple': 0.40, 'banana': 0.50}
        my_purchase = {
            'apple': 1,
            'banana': 6}
        grocery_bill = sum(prices[fruit] * my_purchase[fruit] for fruit in my_purchase)
        activities = {8: 'Sleeping',9: 'Commuting', 17: 'Working', 18: 'Commuting',20: 'Eating', 22: 'Resting' }
        time_now = localtime()
        hour = time_now.tm_hour

        for activity_time in sorted(activities.keys()):
            if hour < activity_time:
                a = activities[activity_time]
                break
            else:
                a ='Unknown, AFK or sleeping!'
        
        my_account = BankAccount(15)
        my_account.withdraw(50)
        
        for answer in solve(BOARD_SIZE):
            a = answer
        for p in iter_primes():
            if p > 20:
                break
            a = p

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("tasks()", setup="from __main__ import tasks", number=5000))