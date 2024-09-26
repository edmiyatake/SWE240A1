# SWE240 Assignment 1 Edwin Miyatake
# Goal is to implement a data structure that can function as a bank account
# Each bank account needs a name, address, social security, and an initial deposit
class Users:
    def __init__(self,val):
        self.val = val
        self.next = None


class BankAccount:
    def __init__(self,name,add,ssn,deposit,users):
        # Initial Properties
        self.name = name
        self.add = add
        self.ssn = ssn
        self.deposit = deposit
        # Task 1: sorted linked list to record users
        # I think that it should just store the head of the LL
        self.users = users 

ds