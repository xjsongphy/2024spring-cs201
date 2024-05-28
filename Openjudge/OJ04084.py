"""于2024-5-22测试通过"""
from heapq import *

v, a = map(int, input().split())
edges = {i: {} for i in range(1, v + 1)}
for _ in range(a):
    f, t = map(int, input().split())
    edges[f][t] = True
in_degree = {i: 0 for i in edges}
for i in edges:
    for j in edges[i]:
        in_degree[j] += 1

heap = []
for i in in_degree:
    if in_degree[i] == 0:
        heap.append(i)

ans = []
heapify(heap)
while heap:
    idx = heappop(heap)
    ans.append('v' + str(idx))
    for i in edges[idx]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            heappush(heap, i)
print(' '.join(ans))