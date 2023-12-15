# Imagine a stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds a threshold.
# Implement a data structure SetOFStacks that mimics this, push and pop methods should work as if it's a single stack
# Additionally, implement popAt(index) which performs pop on a specific sub stack


class SetOfStacks():
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.stack_info = []
        # list of stacks

    def __str__(self) -> str:
        return str(self.stack_info)

    def push(self, value):
        if len(self.stack_info) > 0 and len(self.stack_info[-1]) < self.capacity:
        # if stack is not empty and ele in the last stack is less then capacity, append ele at the last stack
            self.stack_info[-1].append(value)
        else:
            # if stack is empty or exceeds limit, create new stack
            self.stack_info.append([value])
        return self.stack_info

    def pop(self):
        # if len(self.stack_info) ==0:
        #     return "Stack is empty"
        # elif len(self.stack_info) > 0 and self.stack_info[-1] == 0:
        #     # last stack is empty, pop last list first and then last ele
        #     self.stack_info.pop()
        #     value = self.stack_info[-1].pop()
        #     return f"Pop: {value}"
        #     # if will not work in this case because there might be multiple empty lists at the end 
        # else:
        #     value = self.stack_info[-1].pop()
        #     return f"Pop: {value}"
        # if will not work in this case because there might be multiple empty lists at the end 
        ## first pop empty lists and then pop last ele
        while len(self.stack_info) and len(self.stack_info[-1]) ==0:
            self.stack_info.pop()
            # pops empty lists
        if len(self.stack_info) ==0:
            return "Empty Stack"
        else:
            value = self.stack_info[-1].pop()
            return f"POP: {value}"

    def popAt(self,stacknum):
        if self.stack_info[stacknum] ==0:
            return "Empty Stack"
        else:
            return self.stack_info[stacknum].pop()

customStack = SetOfStacks(3)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)
print(customStack.pop())
print(customStack.pop())
customStack.push(5)
customStack.push(6)
customStack.push(7)
customStack.push(8)
print(customStack)
print(customStack.popAt(0))
print(customStack.popAt(1))
