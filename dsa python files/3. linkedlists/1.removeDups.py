# Write a function to remove duplictes from the unsorted linked list

from LinkedList import LinkedList

def removeDups(ll):
    # compare next node's value to uniqueset and remove or go forward accordingly
    if ll.head is None:
        return None
    else:
        node = ll.head
        unique_set = set([node.value]) #using a temp buffer
        while node.next:
            if node.next.value in unique_set:
                #delete next node
                node.next = node.next.next
            else:
                node = node.next
        return ll


#without a temp buffer
def removeDups1(ll):
    if ll.head is None:
        return None
    else:
        currNode = ll.head
        while currNode:                # ------> O(n^2) time complexity
            runner = currNode
            while runner.next:
                if runner.next.value == currNode.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            currNode = currNode.next
        return ll

customLL = LinkedList()
customLL.generate(20, 0, 99)
print(customLL)
print(removeDups(customLL)) # ------> O(n) time complexity
print("***")
print(customLL)
print(removeDups1(customLL)) # ------> O(n^2) time complexity