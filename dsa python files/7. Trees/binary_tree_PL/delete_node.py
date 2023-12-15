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
        
    def delete_node(self, nodeValue):
        if self.lastUsedIndex ==0:
            return "tree is empty"
        for i  in range(1, self.lastUsedIndex+1):
            if self.customList[i]==nodeValue:
                self.customList[i]= self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex]=None
                self.lastUsedIndex-=1
                return "deleted"
        return "not found"
        # time complexity is O(n) since iterating through all elements
        # space complexity is O(1)
    
    def delete_tree(self):
        if self.lastUsedIndex == 0:
            return "tree is already empty"
        else:
            self.customList = [None]

newBt = Tree(7)
newBt.insert_node('Drinks')
newBt.insert_node('Hot')
newBt.insert_node('Cold')
newBt.insert_node('Tea')
newBt.insert_node('Coffee')
newBt.insert_node('Test')
print(newBt)
print("--------")
newBt.delete_node('Test')
print(newBt)
print("--------")
newBt.delete_node('Hot')
print(newBt)
print("---------")
newBt.delete_tree()
print(newBt)