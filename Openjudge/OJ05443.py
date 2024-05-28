"""于2024-4-29测试通过"""
from heapq import  *

p = int(input())
ls = [input() for _ in range(p)]
q = int(input())
edges = {i: {} for i in ls}
for _ in range(q):
    a, b, d = input().split()
    if b in edges[a] and edges[a][b] < int(d):
        continue
    edges[a][b] = edges[b][a] = int(d)
for _ in range(int(input())):
    start, end = input().split()
    visited = {}
    heap = [(0, [start])]
    heapify(heap)
    while True:
        d, ls = heappop(heap)
        place = ls[-1]
        if place in visited and visited[place] <= d:
            continue
        if place == end:
            break
        visited[place] = d
        for to, l in edges[place].items():
            heappush(heap, (d + l, ls + [to]))
    ans = ls[0]
    for i in range(1, len(ls)):
        ans += '->(' + str(edges[ls[i - 1]][ls[i]]) + ')->' + ls[i]
    print(ans)
