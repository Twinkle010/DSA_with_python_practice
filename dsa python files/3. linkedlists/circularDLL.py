class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.prev = None
        self.next = None

class CDLL():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def create(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.next = node
        node.prev = node

    def insert(self, value, location):
        if self.head is None:
            return f"empty list.. can't insert"
        else:
            newNode = Node(value)
            if location==0:
                #insert at beginning
                newNode.prev = self.tail
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location==-1:
                # insert at end
                newNode.prev = self.tail
                newNode.next = self.head
                self.head.prev = newNode
                self.tail.next= newNode
                self.tail = newNode
            else:
                # loop and find prev node
                index =0
                currNode = self.head
                while index<location-1:
                    index+=1
                    currNode = currNode.next
                    if currNode.next == self.tail:
                        break
                newNode.next = currNode.next
                newNode.prev = currNode
                currNode.next.prev= newNode
                currNode.next = newNode
        
    def traversal(self):
        if self.head is None:
            return f"empty list"
        else:
            node = self.head
            while node:
                print(node.value)
                if node == self.tail:
                    break
                node = node.next
    
    def reverse_traversal(self):
        if self.head is None:
            return f"empty list"
        else:
            node = self.tail
            while node:
                print(node.value)
                if node == self.head:
                    break
                node = node.prev

    def search(self, value):
        index = 0
        if self.head is None:
            return f"empty list"
        else:
            node = self.head
            while node:
                if node.value == value:
                    return f"ele found at {index}"
                index+=1
                if node == self.tail:
                    break
                node = node.next
        return f"element not found in the list"

    def delete(self, location):
        if self.head is None:
            return f"empty list.. cant' delete"
        elif self.head == self.tail:
            node = self.head
            node.prev = None
            node.next = None
            self.head = None
            self.tail = None
        else:
            if location ==0 :
                # delete first node
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
            elif location == -1:
                # delete last node
                self.tail = self.tail.prev 
                self.tail.next = self.head
                self.head.prev = self.tail
            else:
                # delte at given index
                index=0
                currNode = self.head
                while index<location-1:
                    index+=1
                    currNode = currNode.next
                currNode.next = currNode.next.next
                currNode.next.prev = currNode

    def delete_list(self):
        if self.head is None:
            return f"empty list"
        else:
            node = self.head
            self.tail.next=None
            while node:
                node.prev = None
                node = node.next
                if node.next == self.head:
                    break
                
            self.head = None
            self.tail=None









circular_doublyLL = CDLL()
circular_doublyLL2 = CDLL()
circular_doublyLL.create(10)
print([node.value for node in circular_doublyLL])
circular_doublyLL2.create(20)
print([node.value for node in circular_doublyLL2])
circular_doublyLL.insert(12, 0)
circular_doublyLL.insert(22, -1)
circular_doublyLL.insert(72, 1)
print([node.value for node in circular_doublyLL])
(circular_doublyLL.traversal())
print([node.value for node in circular_doublyLL])
circular_doublyLL.reverse_traversal()
print(circular_doublyLL.search(12))
print(circular_doublyLL.search(22))
print(circular_doublyLL.search(90))
print([node.value for node in circular_doublyLL])
circular_doublyLL.delete(0)
circular_doublyLL.delete(-1)
circular_doublyLL.delete(1)
print([node.value for node in circular_doublyLL])
circular_doublyLL.delete_list()
print([node.value for node in circular_doublyLL])

