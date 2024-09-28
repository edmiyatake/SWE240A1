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
    def addUser(self,ID = 0, name = "",add = "", ssn = 0, deposit = 0):
        # Assuming that input "user" is a string/name of the user being put in
        newNode = Node(ID,name,add,ssn,deposit)
        self.size += 1

        if self.head is None:
            self.head = newNode
            return 0
        # Order matters so we need prev,curr
        dummy = Node(0)
        dummy.next = self.head
        prev,curr = dummy, self.head
        while curr:
            if newNode.ID == curr.ID:
                print("ID IS ALREADY TAKEN PLEASE CHOOSE ANOTHER")
                break
            elif newNode.ID > prev.ID and newNode.ID < curr.ID:
                prev.next = newNode
                newNode.next = curr
            prev = prev.next
            curr = curr.next
        self.head = dummy.next
        
    # If a user closes their account, the unique ID can be re-claimed and re-assigned to future new users. 
    # not quite sure how to implement this one

    def deleteUser(self,ID):
    # function won't make it to very end of the linked list SOLVED
    # first node gets deleted then head must be changed
        if self.head is None:
            print("LIST IS EMPTY!")
        if self.head.ID == ID:
            print("this part is working")
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
        if self.head is None:
            raise Exception("LIST IS EMPTY")
        
        while curr:
            print(curr.ID)
            curr = curr.next
        
# list1.payUserToUser("42","32",500) # test case works but to check just put print statements on the deposit 
# Maybe i want to make error statements for missing entries or maybe if theres not enough in the balance?
# list1.printList()

# Task 2 test cases

# list1 = LinkedList()
# list1.addUser(42,"Facebook","1 Hacker Way, Menlo Park, CA", 409903135, 25623) # checks initial insert
# list1.addUser(12,"Google","1600 Amphitheatre Parkway, Mountain View, CA", 235524141, 12330) # checks actual insert after first pass
# list1.addUser(32,"Microsoft","1 Microsoft Way, Redmond, WA", 567221425, 46745) # one more random check
# list1.addUser(32,"Microsoft","1 Microsoft Way, Redmond, WA", 567221425, 46745) # testing the unique id check
# # this also shouldn't interfere with task 6 because unique id is required so no repeats are allow
# list1.printList()

# Task 3 test cases

list2 = LinkedList()
list2.addUser(201,"Facebook","1 Hacker Way, Menlo Park, CA", 409903135, 25623) 
list2.addUser(432,"Google","1600 Amphitheatre Parkway, Mountain View, CA", 235524141, 12330) 
list2.addUser(6233,"Microsoft","1 Microsoft Way, Redmond, WA", 567221425, 46745) 
list2.deleteUser(201)
# list2.printList()



# Task 4 test cases

# Task 5 test cases

# Task 6 test cases

# Task 7 test cases




