# You have two numbers represented by a linked list , where each node contains a single digit. 
# The digits are stored in reverse order such that 1's list is stored at the head of the list
# Write the function that adds two numbers and returns the sum as a linked list

from LinkedList import LinkedList
def sumLists(ll1, ll2):
    n1 = ll1.head
    n2 =ll2.head
    carry = 0
    ll = LinkedList()
    while n1 or n2:
        result = carry
        if n1:
            result+=n1.value
            n1 = n1.next
        
        if n2:
            result+=n2.value
            n2 = n2.next

        carry = result / 10
        rem = int(result % 10)
        ll.add(rem)
    ll.add(int(carry))
    return ll

ll1 = LinkedList()
ll1.add(9)
ll1.add(2)
ll1.add(5)
ll2 = LinkedList()
ll2.add(4)
ll2.add(7)
ll2.add(8)
print(ll1)
print(ll2)
print(sumLists(ll1, ll2))