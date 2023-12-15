class Tree():
    def __init__(self, data, children=[]) -> None:
        self.data = data
        self.children = children
    
    def __str__(self, level=0) -> str:
        return_obj = " " * level + str(self.data) + "\n"
        for each_child in self.children:
            return_obj += each_child.__str__(level + 1)
        return return_obj

    def addChild(self, TreeNode):
        self.children.append(TreeNode)

customTree = Tree('Drinks')
hot_tree = Tree('Hot', [])
cold_tree = Tree('Cold', [])
customTree.addChild(hot_tree)
customTree.addChild(cold_tree)
print(customTree)