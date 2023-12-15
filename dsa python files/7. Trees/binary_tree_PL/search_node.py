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
    
    def search_node(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return f"found at index {i}"
        return "not found"

newBt = Tree(4)
newBt.insert_node('Drinks')
newBt.insert_node('Hot')
print(newBt.insert_node('Cold'))

print(newBt)
print("**********")
print(newBt.search_node('Cold'))
print(newBt.search_node('Drinks'))
print(newBt.search_node('Maggie'))