# create a binary tree using python lists
# leave the 0 th position
# place the left child in 2x positions
# place the right Child in 2x+1 positions

class Tree():
    def __init__(self, size) -> None:
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxsize = size

newBT = Tree(8)
# time complexity -O(1)
# space - O(n) since creating list of size