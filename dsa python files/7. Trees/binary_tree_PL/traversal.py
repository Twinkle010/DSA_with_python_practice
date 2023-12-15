class Tree():
    def __init__(self, size) -> None:
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
    
    def __str__(self) -> str:
        ele = [str(x) for x in self.customList]
        return "\n".join(ele)
    
    def insert_node(self, newValue):
        if self.lastUsedIndex+1 == self.maxSize:
            return "tree is already full"
        else:
            self.customList[self.lastUsedIndex+1] = newValue
            self.lastUsedIndex += 1
            return "inserted"
    
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        
        print(self.customList[index])
        self.preOrderTraversal(index*2) # -> O(n/2)
        self.preOrderTraversal(index*2 +1) # -> O(n/2)
        # time: O(n), space -O(1)
    
    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return 
        
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)
    
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return 
        
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])
    
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])
    
newBt = Tree(6)
newBt.insert_node('Drinks')
newBt.insert_node('Hot')
newBt.insert_node('Cold')
newBt.insert_node('Tea')
newBt.insert_node('Coffee')
# print(newBt)
newBt.preOrderTraversal(1)
print("--------")
newBt.inOrderTraversal(1)
print("--------")
newBt.postOrderTraversal(1)
print("--------")
newBt.levelOrderTraversal(1)
