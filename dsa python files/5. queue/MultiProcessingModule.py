from queue import Queue
customQueue = Queue(maxsize=3)
print(customQueue.empty())
print(customQueue.qsize())
customQueue.put(1)
print(customQueue.full())
print(customQueue.get())
print(customQueue.empty())
