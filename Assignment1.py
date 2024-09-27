# SWE240 Assignment 1 Edwin Miyatake
# Goal is to implement a data structure that can function as a bank account
# Each bank account needs a name, address, social security, and an initial deposit
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    # Task 2 is a function that appeneds a user to a list and updates size/users
    def addUser(self, user):
        # Assuming that input "user" is a string/name of the user being put in
        newNode = Node(user)
        self.size += 1
        newNode.next = None
        if self.head is None:
            self.head = newNode
        if self.tail is None:
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def printList(self):
        curr = self.head
        print(self.size)
        while curr:
            print(curr.val)
            curr = curr.next

list1 = LinkedList()
list1.addUser("42")
list1.addUser("32")
list1.addUser("72")
list1.addUser("99")
list1.printList()


