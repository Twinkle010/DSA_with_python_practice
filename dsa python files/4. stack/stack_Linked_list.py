class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
    def __str__(self) -> str:
        return str(self.value)

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def __len__(self):
        node = self.head
        count=0
        while node:
            count+=1
            node = node.next
        return count

    def insert(self, value, location):
        node = Node(value)
        if self.head == None:
            self.head = node
            node.next = None
            self.tail =  None
        elif location == 0:
            #insert at the beginning
            node.next = self.head
            self.head = node
        elif location == -1:
            #insert at the end
            head = self.head
            while head:
                head = head.next
            head.next = node
            node.next = None
            self.tail = node
        else:
            # insert at location
            head = self.head
            count = 0
            while head:
                if count == location-1:
                    break
                count+=1
                head = head.next
            node.next = head.next
            head.next = node
    
    def pop(self):
        #stack pops out the head ele
        if self.head is None:
            return "Empty list"
        else:
            head = self.head.value
            self.head = self.head.next
            return head
    
    def delete(self):
        if self.head is not None:
            self.head = None
        

class Stack():
    def __init__(self) -> None:
        list = LinkedList()
        self.list = list
    
    def __str__(self) -> str:
        values = [str(x) for x in self.list]
        return '->'.join(values)
    
    def isEmpty(self):
        if len(self.list) == 0:
            # or if head points to none
            return True
        else:
            return False
    
    def push(self, value):
        #LIFO
        self.list.insert(value, location=0)
        return self.list
    
    def pop(self):
        if len(self.list) ==0:
            return "Stack is empty"
        else:
            value = self.list.pop()
            return f"Popped item: {value}"
    
    def peek(self):
        if len(self.list) ==0:
            return "Stack is empty"
        else:
            return self.list.head.value
    
    def delete(self):
        self.list.delete()

customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)
print(customStack.pop())
print(customStack)
print(customStack.peek())
print(customStack.isEmpty())
customStack.delete()
print(customStack)
print(customStack.pop())
