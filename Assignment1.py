# SWE240 Assignment 1 Edwin Miyatake
# Goal is to implement a data structure that can function as a bank account
# Each bank account needs a name, address, social security, and an initial deposit
# User account equivalent would be a node which should hold all the IDs, data, etc.
class Node:
    def __init__(self,ID = 0, name = "",add = "", ssn = 0, deposit = 0):
        self.name = name
        self.add = add
        self.ssn = ssn
        self.deposit = 0
        self.ID = ID # can size and ID be the same thing? -> better is to hold size in linkedlist class and assign into the node
        # can't be the same because they conflict when removing an user
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.ID = 0
        self.size = 0
    
    # Task 2 is a function that appeneds a user to a list and updates size/users
    # opening an acc means that a new user is assigned an ID
    def addUser(self, user):
        # Assuming that input "user" is a string/name of the user being put in
        newNode = Node(user)
        self.size += 1
        self.ID += 1 # can increment by whatever to make the ID 
        newNode.next = None
        if self.head is None:
            self.head = newNode
        if self.tail is None:
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    # If a user closes their account, the unique ID can be re-claimed and re-assigned to future new users. 
    # not quite sure how to implement this one

    def deleteUser(self,ID):
    # function won't make it to very end of the linked list 
        dummy = Node(0)
        dummy.next = self.head
        prev, curr = dummy, self.head
        while curr:
            if curr.ID == ID:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        self.head = dummy.next
        self.size -= 1


    def payUserToUser(self,ID1,ID2,amount):
        curr = self.head
        while curr:
            if curr.ID == ID1:
                curr.deposit = curr.deposit - amount
            elif curr.ID == ID2:
                curr.deposit = curr.deposit + amount
            curr = curr.next
        return 0

    # if its odd, return the middle node X[(n + 1)/2]
    # if its even, return the average of the two nodes and return the first middle node   (X[n/2] + X[(n/2) + 1]) / 2 and return X[n/2] 
    def getMedianID(self):
        if self.head is None:
           raise Exception("List is empty!")
        n = self.size

        if n % 2 == 1:
           medianIndex = (n + 1) // 2
           curr, counter = self.head, 1
           while curr:
               if counter == medianIndex:
                   return f"The median of the linked list has the ID: {curr.ID}"
               counter += 1
               curr = curr.next
        else:
           medianIndex = n // 2
           curr, counter = self.head, 1
           while curr:
               if counter == medianIndex:
                   solution = (int(curr.ID) + int(curr.next.ID)) / 2
                   return f"The average ID of the two middle nodes is {solution} and the first middle node is {curr.ID}"
               counter += 1
               curr = curr.next
        return -1
                  
        
    def printList(self):
        curr = self.head
        #print(self.size)
        while curr:
            print(curr.ID)
            curr = curr.next
        

list1 = LinkedList()
list1.addUser("42")
list1.addUser("32")
list1.addUser("72")
list1.addUser("99")
list1.deleteUser("42")
list1.deleteUser("99")
# list1.payUserToUser("42","32",500) # test case works but to check just put print statements on the deposit 
# Maybe i want to make error statements for missing entries or maybe if theres not enough in the balance?
# list1.printList()
print(list1.getMedianID())



