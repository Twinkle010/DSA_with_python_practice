class Queue:
    def __init__(self) -> None:
        self.items = []
    
    def __str__(self) -> str:
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        
    def enqueue(self, value):
        self.items.append(value)
        return f"enqueued item to queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            value = self.items.pop(0)
            return f"Dequeued: {value}"
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return f"Peek: {self.items[0]}"
    
    def delete(self):
        self.items = []

customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue)
print(customQueue.peek())
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())
customQueue.delete()
print(customQueue)

