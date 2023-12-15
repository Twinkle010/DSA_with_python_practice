class CircularQueue():
    def __init__(self, maxSize) -> None:
        self.maxSize = maxSize
        self.items = maxSize * [None]
        self.start = -1
        self.top = -1
    
    def __str__(self) -> str:
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.top==-1:
            return True
        elif self.start == self.top:
            return True
        else:
            return False
    
    def isFull(self):
        if self.start == self.top +1:
            return True
        elif self.start == 0 and self.top +1== self.maxSize:
            return True
        else:
            return False
    
    def enqueue(self, value):
        if self.isFull():
            return "Queue is full"
        else:
            # increment top and place value
            # if top is at last postition and queue is not full, update top to first ele(circular)
            if self.top +1 == self.maxSize:
                self.top = 0
            else:
                self.top +=1
                if self.start == -1:
                    # if no ele is in queue yet
                    self.start = 0
            self.items[self.top] = value
        return "Enqueued"
    
    def dequeue(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            value = self.items[self.start]
            start =  self.start
            # if start ele is at the end, bring it to the first
            if self.start +1==self.maxSize:
                self.start=0
            elif self.start==self.top:
                #if it;s the last ele in the queue, empty the queue
                self.start = -1
                self.top = -1
            else:
                self.start+=1
            self.items[start]= None
            return f"Dequeued: {value}"

customQueue = CircularQueue(4)
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue)
print(customQueue.isFull())
print(customQueue.dequeue())
print(customQueue)
print(customQueue.start, customQueue.top)
print(customQueue.dequeue())
print(customQueue.start, customQueue.top)
print(customQueue.dequeue())
print(customQueue.start, customQueue.top)
print(customQueue)
customQueue.enqueue(5)
print(customQueue)
customQueue.enqueue(6)
customQueue.enqueue(7)
customQueue.enqueue(8)
# print(customQueue.dequeue())
print(customQueue.start, customQueue.top)
print(customQueue)

# print(customQueue.dequeue())
print(customQueue.start, customQueue.top)
print(customQueue)
print(customQueue.enqueue(8))

