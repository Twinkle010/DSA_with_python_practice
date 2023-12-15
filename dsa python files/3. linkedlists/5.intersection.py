# check if two lists are intersecting i.e have a same reference
# return intersecting node 
# ex : 3->4->5->   ----
#2. 1->2->3->      ----
# intersection: ->6->7
# return 6

from LinkedList import LinkedList, Node

def intersection(ll1, ll2):
    # check if two lists are equal,
    # if len are not equal, remove first diff nodes and loop and validate
    # if tails are not equal , no intersection
    if ll1.tail is not ll2.tail:
        return None
    else:
        # find difference between lists
        len1 = len(ll1)
        len2 = len(ll2)
        short_node = ll1 if len1 < len2 else ll2
        long_node = ll2 if len1 > len2 else ll2

        diff = len(long_node) - len(short_node)
        longer_node = long_node.head
        shorter_node = short_node.head

        for i in range(diff):
            longer_node = longer_node.next

        # now both nodes are at same point
        while longer_node is not shorter_node:
            longer_node = longer_node.next
            shorter_node = shorter_node.next
        return longer_node

# helper method to add same tail to ll
def add_tail(ll1, ll2, value):
    node_value = Node(value)
    ll1.tail.next = node_value
    ll1.tail = node_value
    ll2.tail.next = node_value
    ll2.tail = node_value
    return ll1, ll2


llA = LinkedList()
llA.add(9)
llA.add(19)
llA.add(29)

llB= LinkedList()
llB.add(2)
llB.add(22)
llB.add(32)
llB.add(42)
llB.add(52)

add_tail(llA, llB, 10)
add_tail(llA, llB, 100)
print(llA)
print(llB)
print(intersection(llA, llB))

