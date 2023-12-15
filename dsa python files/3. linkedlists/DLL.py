class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.prev =None

class DLL():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def create(self, value):
        node = Node()
        node.value = value
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
    
    def insert(self, value, location):
        node = Node(value)
        if location == 0:
            if self.head is None:
                self.head = node
                self.tail = node
                node.prev = None
                node.next = None
            else:
                #insert at beginning
                node.next = self.head
                node.prev = None
                self.head.prev = node
                self.head = node
        elif location==-1:
            if self.head is None:
                return f"the list is empty, can't insert"
            else:
                #insert at the end
                node.prev = self.tail
                node.next = None
                self.tail.next = node
                self.tail = node
        else:
            #insert at given location
            #find prev node
            index = 0
            currNode = self.head
            while index<location-1:
                index+=1
                currNode = currNode.next
            node.next = currNode.next
            node.prev = currNode
            currNode.next.prev = node
            currNode.next = node
    
    def traversal(self):
        if self.head is None:
            return f"empty list"
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
    
    def reverse_traversal(self):
        if self.head is None:
            return "empty list"
        else:
            node = self.tail
            while node:
                print(node.value)
                node = node.prev
    def search(self, value):
        if self.head is None:
            return f"empty list, element not found"
        else:
            node = self.head
            index=0
            while node:
                if node.value == value:
                    return f"element {value} found at {index}"
                index+=1
                node = node.next
            return f"element {value} not found in list"
    
    def delete(self, location):
        if self.head is None:
            return f"list is already empty"
        elif self.head == self.tail: # only one node
            self.head = None
            self.tail = None
        else:
            node = self.head
            if location == 0:
                # delete first node
                self.head = self.head.next
                self.head.prev = None
            elif location == -1:
                #delete last node
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                # delete at a given location
                # loop and find prev node
                currNode = self.head
                index = 0 
                while index < location-1:
                    index+=1
                    currNode = currNode.next
                node_to_del = currNode.next
                node_to_del.next.prev = currNode
                currNode.next = node_to_del.next

    def delete_DLL(self):
        if self.head is None:
            return f"list is already empty"
        else:
            # garbage collector deletes a node if no other node is pointing to this node
            # since in dll, nodes point to prev references, garbage collector will not delete
            node = self.head
            while node:
                node.prev = None
                node = node.next
            self.head = None
            self.tail = None


doublyLL = DLL()
doublyLL.create(5)
doublyLL2 = DLL()
doublyLL2.create(15)
print([node.value for node in doublyLL])

doublyLL.insert(2,0)
doublyLL.insert(4,0)
doublyLL.insert(14,-1)
doublyLL.insert(12,-1)
doublyLL.insert(10,2)
doublyLL.insert(11,2)
print([node.value for node in doublyLL])

doublyLL.traversal()
print("***")
doublyLL.reverse_traversal()
print(doublyLL.search(2))
print(doublyLL.search(22))

print([node.value for node in doublyLL])
doublyLL.delete(0)
print([node.value for node in doublyLL])
doublyLL.delete(-1)
print([node.value for node in doublyLL])
doublyLL.delete(2)
doublyLL.delete(2)
print([node.value for node in doublyLL])
print([node.value for node in doublyLL2])
doublyLL2.delete(15)
print([node.value for node in doublyLL2])

print([node.value for node in doublyLL])
doublyLL.delete_DLL()
print([node.value for node in doublyLL])





        