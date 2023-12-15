from queue import Queue
customQueue = Queue(maxsize=3)
print(customQueue.qsize())
print(customQueue.empty())
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.full())
print(customQueue.qsize())
print(customQueue)
print(customQueue.get())
print(customQueue.qsize())


# task_done, join methods