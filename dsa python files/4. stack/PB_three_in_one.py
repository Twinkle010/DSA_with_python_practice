# Create three stacks in a single python list
# Approach: Split the list into equal number of parts as required
class MultiStack:
    def __init__(self, eachStackSize) -> None:
        self.number_of_stacks = 3 # create 3 stacks
        self.customList = [0] * eachStackSize * self.number_of_stacks # initialise python list
        self.stack_ele_len = [0] * self.number_of_stacks # stack_ele_len to track ele in the list [0,0,0]
        self.eachStackSize = eachStackSize # each stack size
    
    def __str__(self) -> str:
        values = [str(x) for x in self.customList]
        return ' '.join(values)
    
    def isEmpty(self, stacknum):
        if self.stack_ele_len[stacknum] == 0:
            return True
        else:
            return False
    
    def isFull(self, stacknum):
        if self.stack_ele_len[stacknum] == self.eachStackSize:
            return True
        else:
            return False
    
    def getIndexTop(self, stacknum):
        offset = stacknum * self.number_of_stacks
        return offset  + self.stack_ele_len[stacknum] -1# index of this stack + prev no of ele
    
    def push(self, stacknum, value):
        if self.isFull(stacknum):
            return f"Stack is already full"
        else:
            self.stack_ele_len[stacknum] +=1
            self.customList[self.getIndexTop(stacknum)] = value
            return 
    
    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return "Stack is empty"
        else:
            value = self.customList[self.getIndexTop(stacknum)]
            self.customList[self.getIndexTop(stacknum)] = 0
            self.stack_ele_len[stacknum] -= 1
            return f"Popped item: {value}"
    
    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return "Stack is empty"
        else:
            value = self.customList[self.getIndexTop(stacknum)]
            return f"peek item: {value}"

customStack = MultiStack(3)
print(customStack.pop(2))
customStack.push(1,1)
customStack.push(1,2)
customStack.push(1,3)
print(customStack.push(1,4))
print(customStack)
print(customStack.isFull(1))
print(customStack.peek(2))
print(customStack.peek(1))
print(customStack.pop(1))
print(customStack)
