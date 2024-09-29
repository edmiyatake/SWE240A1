class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.ID = [1]

    def uniqueID(self):
        counter = 1
        while counter in self.ID:
            counter += 1
        return counter

    def push(self):
        newNode = Node()
        if self.head == None:
            self.head = newNode
            return 
        elif self.head.next is None and newNode.val < self.head.val:
            newNode.next = self.head
            self.head = newNode
            return
        else:
            curr = self.head
            while curr:
                if newNode.val > curr.val:
                    break
                curr = curr.next
            curr.next = newNode

    def printList(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
    
list1 = LinkedList()
print(list1.uniqueID())
list1.printList()



