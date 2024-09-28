# SWE240 Assignment 1 Edwin Miyatake
# Goal is to implement a data structure that can function as a bank account
# Each bank account needs a name, address, social security, and an initial deposit
# User account equivalent would be a node which should hold all the IDs, data, etc.
class Node:
    def __init__(self,ID = 0, name = "",add = "", ssn = 0, deposit = 0):
        self.name = name
        self.add = add
        self.ssn = ssn
        self.deposit = deposit
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
    def addUser(self,ID = None, name = None,add = None, ssn = None, deposit = None):
        # initialize newNode
        newNode = Node(ID,name,add,ssn,deposit)
        # 3 cases that I can see to insert
        
        # the linked list is empty and I can just use head to point to newNode
        if self.head is None:
            newNode.next = self.head
            self.head = newNode
            
        # the linked list has just head and the newNode value is less than head
        # basically a swap
        elif self.head.ID >= newNode.ID:
            newNode.next = self.head
            self.head = newNode
        else:
            # goal is to find the next largest item after newNode
            curr = self.head
            while curr.next and curr.next.ID < newNode.ID:
                curr = curr.next
            newNode.next = curr.next
            curr.next = newNode.next
        self.size += 1
        
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
        # curr = self.head
        # while curr:
        #     if curr.ID == ID1:
        #         print(f"{curr.ID}'s initial balance is {curr.deposit}")
        #         curr.deposit = curr.deposit - amount
        #         print(f"{curr.ID}'s final balance is {curr.deposit}")
        #     curr = curr.next
        curr1 = self.head
        print(curr1.ID)
        while curr1:
            if curr1.ID == ID2:
                print(f"{curr1.ID}'s initial balance is {curr1.deposit}")
                curr1.deposit = curr1.deposit + amount
                print(f"{curr1.ID}'s final balance is {curr1.deposit}")
            curr1 = curr1.next

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

list1 = LinkedList()
list1.addUser(5,"Facebook","1 Hacker Way, Menlo Park, CA", 409903135, 25623) # checks initial insert
list1.addUser(2,"Google","1600 Amphitheatre Parkway, Mountain View, CA", 235524141, 12330) # checks actual insert after first pass
list1.addUser(3,"Microsoft","1 Microsoft Way, Redmond, WA", 567221425, 46745) # one more random check
# list1.addUser(32,"Microsoft","1 Microsoft Way, Redmond, WA", 567221425, 46745) # testing the unique id check
# # this also shouldn't interfere with task 6 because unique id is required so no repeats are allow
list1.printList()

# Task 3 test cases

# list2 = LinkedList()
# list2.addUser(201,"Facebook","1 Hacker Way, Menlo Park, CA", 409903135, 25623) 
# list2.addUser(432,"Google","1600 Amphitheatre Parkway, Mountain View, CA", 235524141, 12330) 
# list2.addUser(6233,"Microsoft","1 Microsoft Way, Redmond, WA", 567221425, 46745) 
# list2.deleteUser(201)
# list2.printList()

# Task 4 test cases

# list3 = LinkedList()
# list3.addUser(201,"Facebook","1 Hacker Way, Menlo Park, CA", 409903135, 25623) 
# list3.addUser(432,"Google","1600 Amphitheatre Parkway, Mountain View, CA", 235524141, 12330) 
# list3.addUser(6233,"Microsoft","1 Microsoft Way, Redmond, WA", 567221425, 46745) 
# list3.printList()
# list3.payUserToUser(201,432,1000)



# Task 5 test cases

# Task 6 test cases

# Task 7 test cases




