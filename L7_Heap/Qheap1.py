import queue

def getMin():
    return pq.queue[0]

n = int(input())
pq = queue.PriorityQueue()
pqRemove = queue.PriorityQueue()
for i in range(n):
    rawData = input().split()
    t = int(rawData[0])
    if t == 1:
        v = int(rawData[1])
        pq.put(v)
    if t == 2:
        v = int(rawData[1])
        pqRemove.put(v)

    if t == 3:
       while not pqRemove.empty() and pqRemove.queue[0] == getMin():
           pqRemove.get()
           pq.get()
       print(getMin())
