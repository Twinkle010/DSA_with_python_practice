# circular singly linked list
# creation
# create a node
# reference of the node to itself
# assign node to head and tail

class Node():
    def __init__(self, value = None) -> None:
        self.value = value
        self.next = None

class CLL():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.head:
                break

    def createCLL(self, value):
        node = Node()
        node.value = value
        node.next = node
        self.head = node
        self.tail = node

    def insert_value(self, value, location):
        node = Node()
        node.value = value
        if self.head is None:
            return f"the list is empty"
        else:
            if location==0:
                # insert at the begining
                node.next = self.head
                self.head = node
                self.tail.next = node
            elif location==-1:
                # insert at the end 
                node.next = self.tail.next
                self.tail.next = node
                self.tail = node
            else:
                # insert at a location
                tempNode = self.head
                index=0
                while index < location -1:
                    tempNode = tempNode.next
                    index +=1
                node.next = tempNode.next
                tempNode.next = node

    def traversal(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
            if node == self.tail.next:
                break
    
    def search(self, element):
        node = self.head
        index = 0
        while node is not None:
            if node.value == element:
                return f"element found at index {index}"
            index += 1
            node = node.next
            if node.next == self.tail.next:
                break
        
        return f"{element} doesnot exist in the given linkedlist"
            
    def delete_node(self,location):
        if self.head is None:
            return f"the list is empty"
        else:
            if location==0:
                #delete first node
                if self.head.next==self.tail.next:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head.next==self.tail.next:
                    self.head = None
                    self.tail = None
                else:
                    node= self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    currNode = node
                    currNode.next = self.tail.next
                    self.tail = currNode
                    self.tail.next = currNode.next
            else:
                if self.head.next==self.tail.next:
                    self.head = None
                    self.tail = None
                else:
                    index = 0
                    node = self.head
                    while index <location-1:
                        node = node.next
                    node.next = node.next.next
    
    def delete_list(self):
        if self.head is None:
            return f"the list is already empty"
        else:
            self.head = None
            self.tail.next = None
            self.tail = None





circularLL = CLL()
circularLL.createCLL(2)
print([node.value for node in circularLL])
circularLL.insert_value(4,0)
circularLL.insert_value(1,-1)
print([node.value for node in circularLL])
circularLL.insert_value(5,2)
circularLL.insert_value(3,2)
print([node.value for node in circularLL])
circularLL.traversal()
print(circularLL.search(2))
print(circularLL.search(12))

print([node.value for node in circularLL])
circularLL.delete_node(0)
print([node.value for node in circularLL])
circularLL.delete_node(-1)
print([node.value for node in circularLL])
circularLL.delete_node(1)
print([node.value for node in circularLL])
circularLL.delete_node(-1)
print([node.value for node in circularLL])
circularLL.delete_list()
print([node.value for node in circularLL])
print(circularLL.delete_list())

