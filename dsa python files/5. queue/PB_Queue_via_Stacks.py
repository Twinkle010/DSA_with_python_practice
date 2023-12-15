# Implement a Queue using stacks
# diff btw queue and stack -> pop method LIFO and FIFO
# Take two stacks one for temp storage while dequeuing

class Stack():
    def __init__(self) -> None:
        self.list = []

    def __len__(self):
        return len(self.list)
    
    def __str__(self) -> str:
        return str(self.list)

    def push(self, value):
        self.list.append(value)
        return
    
    def pop(self):
        return self.list.pop()

class Queue():
    def __init__(self) -> None:
        self.stack = Stack()
        self.tempStack = Stack()

    def __str__(self) -> str:
        return str(self.stack)
    
    def enqueue(self, value):
        self.stack.push(value)
        return 
    
    def dequeue(self):
        while len(self.stack):
            self.tempStack.push(self.stack.pop())
        # psuhed all ele to new stack
        value = self.tempStack.pop()
        while len(self.tempStack):
            self.stack.push(self.tempStack.pop())
        return value

customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print(customQueue.dequeue())
print(customQueue.dequeue())
print(customQueue.dequeue())
print(customQueue)
