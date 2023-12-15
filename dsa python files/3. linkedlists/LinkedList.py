from random import randint


class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return str(self.value)

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def __str__(self) -> str:
        values= [str(x.value) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        if self.head is None:
            return f"empty list"
        else:
            count = 0
            node = self.head
            while node:
                count+=1
                node =node.next
            return count

    def add(self, value):
        node = Node(value)
        # adding new value at the end of list
        if self.head is None:
            self.head= node
            self.tail= node
            node.next = None
        else:
            self.tail.next = node
            self.tail = node
        return self
        
    def generate(self, n, min_value, max_value):
        # to generate a random linked list
        self.head=None
        self.tail=None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self

# customLL = LinkedList()
# customLL.add(3)
# customLL.add(13)
# print(customLL)

# customLL2 = LinkedList()
# customLL2.generate(10, 0, 99)
# print(customLL2)
# print(len(customLL2))