# 1. create head and tail, intialize with null
# 2. create a node with data
# 3. link head and tail with this node

class Slinkedlist:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node =  node.next

    def insert_ele(self, value, location):
        node = Node(value)
        if self.head == None:
            # ll is empty
            self.head = node
            self.tail = node
        else:
            if location == 0:
                # insert at the beginning
                node.next = self.head
                self.head = node
            elif location == -1:
                #insert at the end
                self.tail.next= node
                self.tail = node
            else:
                # insert at a spcefic location
                # loop over the linked list and insert
                current_node = self.head
                index = 0
                while index < location - 1:
                    current_node = current_node.next
                    index+=1
                node.next = current_node.next
                current_node.next = node
    
    def traverseLL(self):
        if self.head is not None:
            tempNode = self.head
            while tempNode is not None:
                print(tempNode.value)
                tempNode = tempNode.next
        else:
            return None

    def search(self, element):
        if self.head is not None:
            tempNode = self.head
            index = 0 
            while tempNode is not None:
                if tempNode.value == element:
                    return f"eleement found at {index}"
                else:
                    index +=1
                    tempNode = tempNode.next
        else:
            return f"list is empty"
        return f"element doesn't exis"

    def delete_node(self, location):
        if self.head is None:
            return f"the list is empty"
        else:
            if location == 0:
                # delete first node
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    self.head = tempNode.next
            elif location == -1:
                # delete last node
                tempNode = self.head
                # find node before last
                while tempNode is not None:
                    if tempNode.next == self.tail:
                        break
                    tempNode = tempNode.next
                tempNode.next = None
                self.tail = tempNode
            else:
                # loop over and del
                index = 0
                tempNode = self.head
                while index < location - 1:
                    index +=1
                    tempNode = tempNode.next
                node_to_del = tempNode.next
                nextNode = node_to_del.next
                tempNode.next = nextNode

    def delete_linked_list(self):
        if self.head is None:
            return f"list is empty"
        else:
            self.head = None
            self.tail = None

        

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


slinkedlist1= Slinkedlist()
node1=Node()
node2=Node()
slinkedlist1.head = node1
node1.next = node2
slinkedlist1.tail = node2
print([node.value for node in slinkedlist1])


slinkedlist1.insert_ele(1, 0)
slinkedlist1.insert_ele(2, 0)
slinkedlist1.insert_ele(3, 0)
slinkedlist1.insert_ele(4, 0)
slinkedlist1.insert_ele(5, 0)

print([node.value for node in slinkedlist1])

slinkedlist1.insert_ele(2, 1)
slinkedlist1.insert_ele(2, 3)

print([node.value for node in slinkedlist1])
print(slinkedlist1.traverseLL())
print(slinkedlist1.search(2))
print(slinkedlist1.search(12))


print(slinkedlist1.delete_node(2))
print([node.value for node in slinkedlist1])
print(slinkedlist1.delete_node(-1))
print([node.value for node in slinkedlist1])
print(slinkedlist1.delete_node(0))
print([node.value for node in slinkedlist1])

print(slinkedlist1.delete_linked_list())
print([node.value for node in slinkedlist1])
