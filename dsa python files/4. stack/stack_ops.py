class Stack:
    def __init__(self) -> None:
        self.list = []
    
    def __str__(self) -> str:
        list = reversed(self.list)
        ele = [str(x) for x in list]
        return '\n'.join(ele)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def push(self, value):
        self.list.append(value)
        return 'inserted successfully'
    
    def pop(self):
        if self.isEmpty():
            return 'no elements in stack'
        value = self.list.pop()
        return f'popped item: {value}'

    def peek(self):
        if self.isEmpty():
            return 'no elements in stack'
        return f'peek item: {self.list[-1]}'
    
    def delete(self):
        if self.isEmpty():
            return 'Stack is already empty'
        self.list = []

customStack = Stack()
customStack2 = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack2.pop())
print(customStack.pop())
print(customStack2.peek())
print(customStack.peek())
print(customStack)
customStack.delete()
print(customStack)
print("*done*")