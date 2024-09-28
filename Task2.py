class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,val):
        newNode = Node(val)
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
list1.push(5)
list1.push(10)
list1.push(2)
list1.printList()



