# Design a stack which, in addition to push and pop, has a fn which returns min ele?
# push, pop and min all should operate in O(1)
# linked list

class Node():
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        values = str(self.value)
        if self.next:
            values += str(self.next)
        return ' , '.join(values)


class Stack():
    def __init__(self) -> None:
        self.top = None
        self.minNode = None

    def min(self):
        if self.minNode is None:
            return None
        return self.minNode.value

    def push(self, value):
        if self.minNode and (self.minNode.value < value):
            self.minNode = Node(self.minNode.value, next = self.minNode)
        else:
            self.minNode = Node(value, next = self.minNode)
        self.top = Node(value, next=self.top)
    
    def pop(self):
        self.minNode = self.minNode.next
        item = self.top.value
        self.top = self.top.next
        return f"Pop: {item}"
    
    def peek(self):
        return f"Peek: {self.top.value}"

customStack = Stack()
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack.min())
customStack.push(1)
print(customStack.min())
customStack.push(10)
print(customStack.peek())
print(customStack.pop())


        