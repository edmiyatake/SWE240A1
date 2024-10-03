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
        self.ID = [0]

    def assignUniqueID(self):
            counter = 1
            while counter in self.ID:
                counter += 1
            self.ID.append(counter)
            return counter
    
    # Task 2 is a function that appeneds a user to a list and updates size/users
    # opening an acc means that a new user is assigned an ID
    def addUser(self, name = None,add = None, ssn = None, deposit = None):
        # initialize newNode
        ID = self.assignUniqueID()
        newNode = Node(ID,name,add,ssn,deposit)
        # 3 cases that I can see to insert
        if self.head is None:
            self.head = newNode
        elif ID < self.head.ID:
            # make a pointer before head
            dummy = Node(0)
            dummy.next = self.head
            # perform the swap
            dummy.next = newNode
            newNode.next = self.head
            self.head = newNode
        else:
            prev, curr = self.head, self.head.next
            while curr:
                if newNode.ID > prev.ID and newNode.ID < curr.ID:
                    break
                prev, curr = curr,curr.next
            # the two ways the code finishes is if it finds a point or it traverses the whole list
            # curr == None means it went through the whole list and we can just place the node at the end
            if curr != None:
                prev.next = newNode
                newNode.next = curr
            # in the event, we have the point where prev represents the spot where the newNode needs to go
            else:
                prev.next = newNode
        return 0

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
        self.ID.remove(ID)


    def payUserToUser(self,ID1,ID2,amount):
        curr = self.head
        while curr:
            if curr.ID == ID1:
                print(f"{curr.ID}'s initial balance is {curr.deposit}")
                curr.deposit = curr.deposit - amount
                print(f"{curr.ID}'s final balance is {curr.deposit}")
            curr = curr.next
        curr1 = self.head
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
        n = len(self.ID) - 1

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
                   solution = (curr.ID + curr.next.ID) / 2
                   return f"The average ID of the two middle nodes is {solution} and the first middle node is {curr.ID}"
               counter += 1
               curr = curr.next

    def mergeAccounts(self,ID1,ID2):
        sameAcc = False
        curr1,curr2 = self.head, self.head
        count1, count2 = 0,0
        while(curr1):
            if curr1.ID == ID1:
                break
            count1 += 1
            curr1 = curr1.next
        while(curr2):
            if curr2.ID == ID2:
                break
            count1 += 1
            curr2 = curr2.next
        if curr1.name == curr2.name and curr1.add == curr2.add and curr1.ssn == curr2.ssn:
            sameAcc = True
        if sameAcc:
            # sum the two balances, delete acc with highest ID
            # if the first ID is larger then the second
            if curr1.ID > curr2.ID:
                curr2.deposit += curr1.deposit
                self.deleteUser(curr1.ID)
            else:
                curr1.deposit += curr2.deposit
                self.deleteUser(curr2.ID)
        else:
            return -1
        
    def mergeBanks(self,list1,list2):
        head = list1.head
        curr = head
        curr2 = list2.head
        while curr:
            print(curr.name)
            print(curr.ID)
            curr = curr.next     
        # all i have to do is connect the last node of list1 to first node of list2 and add len(list1) to all IDS in list 2
        curr = curr2
        while curr2:
            curr2.ID = curr2.ID + len(list1.ID) - 1
            print(curr2.name)
            print(curr2.ID)
            curr2 = curr2.next     
        return 0
        
    def printList(self):
        curr = self.head
        print(self.ID)
        if self.head is None:
            raise Exception("LIST IS EMPTY")
        
        while curr:
            print(curr.ID)
            print(curr.name)
            print(curr.deposit)

            curr = curr.next
        
# list1.payUserToUser("42","32",500) # test case works but to check just put print statements on the deposit 
# Maybe i want to make error statements for missing entries or maybe if theres not enough in the balance?
# list1.printList()

# Task 2 test cases

# list1 = LinkedList()
# list1.addUser("Facebook","1 Hacker Way, Menlo Park, CA", 409903135, 25623) # checks initial insert
# list1.addUser("Google","1600 Amphitheatre Parkway, Mountain View, CA", 235524141, 12330) # checks actual insert after first pass
# list1.addUser("Microsoft","1 Microsoft Way, Redmond, WA", 567221425, 46745) # one more random check
# # list1.addUser(32,"Microsoft","1 Microsoft Way, Redmond, WA", 567221425, 46745) # testing the unique id check
# # # this also shouldn't interfere with task 6 because unique id is required so no repeats are allow
# list1.printList()
# TASK 2 DONE

# Task 3 test cases

# list2 = LinkedList()
# list2.addUser("Facebook","1 Hacker Way, Menlo Park, CA", 409903135, 25623) 
# list2.addUser("Google","1600 Amphitheatre Parkway, Mountain View, CA", 235524141, 12330) 
# list2.addUser("Microsoft","1 Microsoft Way, Redmond, WA", 567221425, 46745) 
# list2.deleteUser(1)
# list2.printList()
# TASK 3 DONE

# Task 4 test cases

# list3 = LinkedList()
# list3.addUser("Facebook","1 Hacker Way, Menlo Park, CA", 409903135, 25623) 
# list3.addUser("Google","1600 Amphitheatre Parkway, Mountain View, CA", 235524141, 12330) 
# list3.addUser("Microsoft","1 Microsoft Way, Redmond, WA", 567221425, 46745) 
# list3.payUserToUser(1,3,1000)
# MORE TEST CASES / ERROR RAISE WHEN BALANCE IN INSUFFICIENT 
# HOWEVER OTHER THAN THAT THE FUNCTION ITSELF WORKS


# Task 5 test cases

# list1 = LinkedList()
# list1.addUser("Facebook","1 Hacker Way, Menlo Park, CA", 409903135, 25623) 
# list1.addUser("Google","1600 Amphitheatre Parkway, Mountain View, CA", 235524141, 12330) 
# list1.addUser("Microsoft","1 Microsoft Way, Redmond, WA", 567221425, 46745) 
# list1.addUser("Discord","444 De Haro St, Suite 200, San Francisco, CA", 726245763, 46745) 
# print(list1.getMedianID())
# TASK 5 DONE

# Task 6 test cases

# list1 = LinkedList()
# list1.addUser("Facebook","1 Hacker Way, Menlo Park, CA", 409903135, 25623) 
# list1.addUser("Discord","444 De Haro St, Suite 200, San Francisco, CA", 726245763, 46745)
# list1.addUser("Google","1600 Amphitheatre Parkway, Mountain View, CA", 235524141, 12330) 
# list1.addUser("Microsoft","1 Microsoft Way, Redmond, WA", 567221425, 46745) 
# list1.addUser("Discord","444 De Haro St, Suite 200, San Francisco, CA", 726245763, 46745)
# list1.mergeAccounts(1,3)
# list1.mergeAccounts(2,5)
# list1.printList()

#TASK 6 DONE

# Task 7 test cases

list1 = LinkedList()
list1.addUser("Facebook","1 Hacker Way, Menlo Park, CA", 409903135, 25623) 
list1.addUser("Discord","444 De Haro St, Suite 200, San Francisco, CA", 726245763, 46745)
list1.addUser("Google","1600 Amphitheatre Parkway, Mountain View, CA", 235524141, 12330) 
list2 = LinkedList()
list2.addUser("Statefarm", "237 Perimeter Center Pkwy NE Sandy Springs, GA", 522102987, 5234440)
list2.addUser("Geico", "14111 Danielson St, Poway, CA", 216781234, 1231265)
list2.addUser("UCI", "401 E. Peltason Drive, Suite 3200, Irvine, CA", 231987654, 213131312)
list1.mergeBanks(list1,list2)
list1.printList()

