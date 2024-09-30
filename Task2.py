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
    
    def addUser(self):
        val = self.assignedUniqueID()
        newNode = Node(val)
        # after this just add to tail
        if self.head is None:
            self.head = newNode
        
        

    def printList(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
    
list1 = LinkedList()
list1.addUser()
list1.addUser()
list1.printList()



