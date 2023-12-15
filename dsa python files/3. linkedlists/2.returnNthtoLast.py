# Implement an algorithm to find nth to last element of a singly linked list

from LinkedList import LinkedList
# def return_nth_to_last(n, ll):
#     #nth to last is n steps from last i.e 2nd to last ele, return last 2 nodes
#     if ll.head is None:
#         return
#     else:
#         currNode = ll.head
#         len_ll = len(ll)
#         while currNode:
#             if len_ll==n:
#                 ll.head = currNode
#                 return ll
#             len_ll -= 1
#             currNode = currNode.next
    
#     return ll

# assuming the len of list is not known
#track using two pointers, return nth element from the end of the list
def return_nth_to_last2(n, ll):
    pointer1= ll.head
    pointer2 = ll.head
    #maintain n difference between pointers so that last nth ele is returned
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    # now pointer 1 is at head, pointer2 is n places ahead pointer1
    # traverse till pointer2 reaches tail, so that pointer1 is n places before tail
    # i.e print nth element from the last, print pointer1
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

        
customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(return_nth_to_last2(5, customLL))
