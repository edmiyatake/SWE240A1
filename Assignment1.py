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

    def deleteUser(self,user):
    # function won't make it to very end of the linked list
    # dummy pointer could work? 
        curr = self.head
        if self.head is None:
            return 0
        while curr.next:
            if curr.next.val == user:
                curr.next = curr.next.next
                self.size -= 1
            curr = curr.next

    def payUserToUser(user1,user2,amount):
        exit
    
    # if its odd, return the middle node
    # if its even, return the average of the two nodes and return the first middle node    
    def getMedianID(self):
        if self.head is None:
            return
        if self.size % 2 == 1:
            left,right = self.head,self.head.next.next
            while right and right.next:
                left = left.next
                right = right.next.next
            print(left.val)
            return 0
        else:
            return -1 
            
        
    def printList(self):
        curr = self.head
        #print(self.size)
        while curr:
            print(curr.val)
            curr = curr.next
        

list1 = LinkedList()
list1.addUser("42")
list1.addUser("32")
list1.addUser("72")
list1.addUser("99")
list1.deleteUser("32")
list1.getMedianID()
#list1.deleteUser("99")
#list1.printList()


