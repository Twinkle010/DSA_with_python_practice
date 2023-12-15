# You have two numbers represented by a linked list , where each node contains a single digit. 
# The digits are stored in reverse order such that 1's list is stored at the head of the list
# Write the function that adds two numbers and returns the sum as a linked list

from LinkedList import LinkedList
def sumLists(ll1, ll2):
    sum1 = 0
    count = 0
    node_1 = ll1.head
    while node_1:
        node_value = node_1.value
        sum1 = sum1 + node_value* pow(10,count)
        node_1 = node_1.next
        count+=1
    num1 = sum1
    sum2 = 0
    count = 0
    node_2 = ll2.head
    while node_2:
        node_value = node_2.value
        sum2 = sum2 + node_value* pow(10,count)
        node_2 = node_2.next
        count+=1
    num2 = sum2
    sum = sum1 + sum2
    values = find_digits(sum)
    ll = LinkedList()
    # for i in
    # ll.add() 
    
def find_digits(n):
    sum= 0
    values=[]
    if n==0:
        return 0
    else:
        rem = n % 10
        n = n/10
        a= find_digits(n)
        values.append(a)
    return values

