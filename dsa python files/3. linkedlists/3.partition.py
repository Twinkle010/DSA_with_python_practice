# Write code to partition a linked list around value x, such that all nodes less than x come before all nodes greater than x
from LinkedList import LinkedList

def partition(ll, x):
    if ll.head is None:
        return
    else:
        currNode = ll.head
        ll.tail = currNode
        # print(ll.tail.value)
        # print(ll.tail.next.value)
        # create a list with first ele and add ele before and after based on x 
        while currNode:
            nextNode = currNode.next
            currNode.next = None
            if currNode.value < x:
                # add to beginning
                currNode.next = ll.head
                ll.head = currNode
            else:
                # add at the end
                ll.tail.next = currNode
                ll.tail = currNode
            currNode = nextNode
        # if all values are less than x, since tail is set to first node, goes to infite loop, set tail ref to none
        if ll.tail.next is not None:
            # print(ll.tail.value)
            # print(ll.tail.next.value)
            # print(ll.tail.next.next.value)
            ll.tail.next = None


customLL = LinkedList()
customLL.generate(10, 0,9)
print(customLL)
partition(customLL, 10)
print(customLL)