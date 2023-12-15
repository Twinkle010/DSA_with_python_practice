class Stack:
    def __init__(self, maxSize) -> None:
        self.maxSize = maxSize
        self.list = []
    
    def __str__(self) -> str:
        stack = reversed(self.list)
        ele = [str(x) for x in stack]
        return '\n'.join(ele)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    
    def push(self, value):
        if self.isFull():
            print("Stack is already full")
            return
        else:
            self.list.append(value)
            return self.list
            
    def pop(self):
        if self.isEmpty():
            return "Stack is already empty"
        else:
            value = self.list.pop()
            return f"Popped item: {value}"
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return f"Peek: {self.list[-1]}"
    
    def delete(self):
        if self.isEmpty:
            return "Stack is already empty"
        else:
            self.list=[]

customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)
customStack.push(5)
print(customStack.pop())
customStack.push(5)
print(customStack)
print(customStack.peek())
customStack.delete()
print(customStack)