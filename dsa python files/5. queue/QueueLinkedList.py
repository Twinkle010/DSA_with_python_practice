class Node:
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

    def __str__(self) -> str:
        node = self.head
        values = []
        while node:
            values.append(node.value)
            node = node.next
        return '->'.join(values)

class Queue():
    def __init__(self) -> None:
        self.linkedlist = LinkedList()
    
    def __str__(self) -> str:
        values = [str(x) for x in self.linkedlist]
        return '->'.join(values)
    
    def isEmpty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False
    
    def enqueue(self, value):
        currNode = Node(value)
        if self.linkedlist.head == None:
            self.linkedlist.head = currNode
            self.linkedlist.tail = currNode
        else:
            self.linkedlist.tail.next = currNode
            self.linkedlist.tail = currNode
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            node = self.linkedlist.head
            self.linkedlist.head = self.linkedlist.head.next
            return f"dequeued: {node.value}"
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            node = self.linkedlist.head
            return f"Peek: {node.value}"

    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None


customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue)
print(customQueue.peek())

print(customQueue.dequeue())
print(customQueue.dequeue())
print(customQueue.dequeue())
print(customQueue.dequeue())
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue)
customQueue.delete()
print(customQueue)
print("*done*")

