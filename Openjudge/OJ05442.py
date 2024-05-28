""""""
from heapq import *
from queue import Queue

n = int(input())
edges = {}
heap = []
for _ in range(n - 1):
    ls = input().split()
    idx = ls[0]
    edges[idx] = {}
    s, v = ls[2::2], ls[3::2]
    for i in range(int(ls[1])):
        heap.append((int(v[i]), idx, s[i]))
        if s[i] not in edges:
            edges[s[i]] = {}
heapify(heap)
ans = 0
while heap:
    value, a, b = heappop(heap)
    q = Queue()
    visited = {}
    q.put(a)
    circle = False
    while not q.empty():
        i = q.get()
        if i in visited:
            continue
        visited[i] = True
        if i == b:
            circle = True
        for j in edges[i]:
            q.put(j)
    if circle:
        continue
    edges[a][b] = edges[b][a] = value
    ans += value
print(ans)