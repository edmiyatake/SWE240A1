class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.ID = [1]

    def assignedUniqueID(self):
            counter = 1
            while counter in self.ID:
                counter += 1
            self.ID.append(counter)
            return counter
    
    def addUser(self,val):
        # val = self.assignedUniqueID()
        # self.ID.append(val) #DONT NEED TO DO THIS ONE BECAUSE ITS IN HELPER FUNCTION
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        elif val < self.head.val:
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
                if newNode.val > prev.val and newNode.val < curr.val:
                    print("Searching for the point")
                    break
                prev, curr = curr,curr.next
            # the two ways the code finishes is if it finds a point or it traverses the whole list
            # curr == None means it went through the whole list and we can just place the node at the end
            print(f"Prev is {prev.val}")
            if curr != None:
                print(f"Curr is {curr.val}")
                print(f"Prev is {prev.val}")
                prev.next = newNode
                newNode.next = curr
            # in the event, we have the point where prev represents the spot where the newNode needs to go
            else:
                print("Curr is None")
                prev.next = newNode
        return 0
            
    def printList(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
    
list1 = LinkedList()
list1.addUser(1)
list1.addUser(3)
list1.addUser(4)
list1.addUser(2)
list1.addUser(0)

list1.printList()



