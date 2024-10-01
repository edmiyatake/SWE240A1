class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.ID = [0]

    def assignedUniqueID(self):
            counter = 1
            while counter in self.ID:
                counter += 1
            self.ID.append(counter)
            return counter
    
    def addUser(self):
        val = self.assignedUniqueID()
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
    
    def deleteUser(self,val):
        if self.head is None:
            print("LIST IS EMPTY!")
        dummy = Node(0)
        dummy.next = self.head
        prev, curr = dummy, self.head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        self.head = dummy.next
        self.ID.remove(val)

            
    def printList(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
    
list1 = LinkedList()
list1.addUser()
list1.addUser()
list1.addUser()
list1.deleteUser(2)
list1.addUser()

list1.printList()



