class Tree():
    def __init__(self, size) -> None:
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxsize = size
    
    def __str__(self) -> str:
        ele =  (str(x) for x in self.customList)
        return "\n".join(ele)
    
    def insert_node(self, newValue):
        if self.lastUsedIndex+1 == self.maxsize:
            return "tree is already full"
        else:
            self.customList[self.lastUsedIndex+1] = newValue
            self.lastUsedIndex += 1
            return "inserted"

newBt = Tree(3)
newBt.insert_node('Drinks')
newBt.insert_node('Hot')
print(newBt.insert_node('Cold'))
print(newBt)