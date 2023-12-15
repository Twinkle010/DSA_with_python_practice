# Implement a animal shelter queue
# dequeue any should return oldest animal
#dequeue cat should return oldest cat
# dequeue dog should return oldest dog

class Node():
    # value could be name or serial order and type would be cat or dog
    def __init__(self, value, type) -> None:
        self.value = value
        self.type = type
        self.next = None
        self.prev = None
    
class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def insert(self, value, type):
        # insert at the end (Queue)
        currNode = Node(value, type)
        if self.head is None:
            self.head = currNode
            self.tail = currNode
        else:
            currNode.prev = self.tail
            self.tail.next = currNode
            currNode.next = None
            self.tail = currNode

    def delete(self, type=None):
        if type:
                node = self.head
                while node:
                    if node.type == type:
                        value = node.value
                        if self.head == node:
                            self.head = self.head.next
                            self.head.prev = None
                        else:
                            # prevNode = node.prev
                            # nextNode = node.next
                            # prevNode.next = nextNode
                            node.prev.next = node.next
                            node.prev = None
                            node.next = None
                        return value, type
                    else:
                        if node.next != self.tail:
                            node = node.next
                        else:
                            return f"No {type} available"
        else:
            # in case of pop any, return whatever is head
            value = self.head.value
            type = self.head.type
            self.head = self.head.next
            self.head.prev = None
            return value,type
                    
class AnimaLShelter():
    def __init__(self) -> None:
        self.data = LinkedList()
    
    def __str__(self) -> str:
        currNode = self.data.head
        output = []
        while currNode:
            output.append(currNode.value)
            currNode = currNode.next
        return ' --> '.join([str(x) for x in output])

    def add(self, name, type):
        self.data.insert(name, type)
        return 
    
    def give_any(self):
        oldest_animal = self.data.delete()
        return oldest_animal
    
    def give_Cat(self):
        oldest_cat = self.data.delete("Cat")
        return oldest_cat

    def give_Dog(self):
        oldest_Dog = self.data.delete("Dog")
        return oldest_Dog

customShelter = AnimaLShelter()
customShelter.add("The first Dog", "Dog")
customShelter.add("The second Dog", "Dog")
customShelter.add("The first Cat", "Cat")
customShelter.add("The second Cat", "Cat")
customShelter.add("The third Dog", "Dog")
customShelter.add("The fourth Dog", "Dog")
print(customShelter)
print(customShelter.give_any())
print(customShelter.give_Cat())
print(customShelter.give_Dog())
print(customShelter)

