import queue


class PQEntry:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value


n = int(input())
arr = list(map(int, input().split()))[:n]
pq = queue.PriorityQueue()
for i in range(n):
    pq.put(PQEntry(arr[i]))
    if pq.qsize() < 3:
        print(-1)
    else:
        first = pq.get().value
        second = pq.get().value
        third = pq.get().value
        print(third*second*first)
        pq.put(PQEntry(first))
        pq.put(PQEntry(second))
        pq.put(PQEntry(third))

