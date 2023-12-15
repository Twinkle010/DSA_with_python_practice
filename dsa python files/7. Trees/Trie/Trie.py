class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def __str__(self) -> str:
        current = self.root.children
        return str(current)


    def insertString(self, word):
        # O(m), O(m) if m is number of chars of the word
        # get current node
        currentNode = self.root
        # iterate through the str, insert new node if the charecter doesnot exist
        for i in word:
            ch = i
            # check if ch exists in children
            node = currentNode.children.get(ch)
            if node == None:
                # create new node and insert
                node = TrieNode()
                # link to the currentnode
                currentNode.children.update({ch:node})
            currentNode = node
        currentNode.endOfString = True
        return "Inserted"
    
    def searchString(self, word):
        # loop over the chars of the word 
        currentNode = self.root
        for i in word:
            ch = i
            nextNode = currentNode.children.get(ch)
            if nextNode == None:
                return False
            # else continue with next letters
            currentNode = nextNode
        if currentNode.endOfString == True:
            return True
        else:
            # condition when the word is prefix
            return False


        
def deleteString(root, delWord, index):
    ch = delWord[index]
    currnode = root.children.get(ch)
    canthisNodeBeDeleted = False #maintain a variable to delete node

    if not currnode:
        return False

    #case1: if some other node's prefix is prefix of this word, call method recursively for next index
    if len(currnode.children) > 1:
        deleteString(currnode, delWord, index+1)
        return False # since this cannot be deleted
    
    #case2: we're at last char of the word, but this is prefix of some other word, set eos to false
    if index == len(delWord) - 1:
        if len(currnode.children) >= 1:
            currnode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True
    
    #case3: some other word is prefix of this word
    if currnode.endOfString == True:
        # cannot del current, go to next node
        deleteString(currnode, delWord, index+1)
        return False
    
    #case4: no dependency on existing
    canthisNodeBeDeleted = deleteString(currnode, delWord, index+1)
    if canthisNodeBeDeleted:
        root.children.pop(ch)
        return True
    else:
        return False
        
            
            




customTrie = Trie()
print(customTrie.insertString('API'))
customTrie.insertString('APL')
customTrie.insertString('APLE')
customTrie.insertString('APPL')
customTrie.insertString('CSD')
print(customTrie.searchString("API"))
print(customTrie.searchString("AP"))
print(customTrie.searchString("DSD"))
# print(customTrie)
print("--------")
print("case:1")
print(customTrie.searchString('API'))
deleteString(customTrie.root, 'API', 0)
print(customTrie.searchString('API'))
print("case2")
print(customTrie.searchString('APL'))
deleteString(customTrie.root, 'APL', 0)
print(customTrie.searchString('APL'))
print("case3")
customTrie.insertString('APL')
print(customTrie.searchString('APL'))
print(customTrie.searchString('APLE'))
deleteString(customTrie.root, 'APLE', 0)
print(customTrie.searchString('APLE'))
print("case4")
print(customTrie.searchString('CSD'))
deleteString(customTrie.root, 'CSD', 0)
print(customTrie.searchString('CSD'))
print("-----")
