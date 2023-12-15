from collections import deque

customQueue = deque(maxlen=3)
# if size is given and enqueue overflows , the frst ele is deleted and new ele are inserted
print(customQueue)
customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
print(customQueue)
customQueue.append(4)
print(customQueue)

#dequeue ele 
print(customQueue.popleft())
print(customQueue.pop())
print(customQueue)
customQueue.clear()
print(customQueue)


