"""于2024-6-3测试通过"""
from heapq import *

while True:
    n = int(input())
    if n == 0:
        break

    trucks = [input() for _ in range(n)]

    vertex = {i: False for i in range(n)}
    vertex[0] = True
    distance = [10]*n
    distance[0] = [0]

    def d(a, b):
        return sum([trucks[a][i] != trucks[b][i] for i in range(7)])

    q = 0
    heap = []
    for i in range(1, n):
        t = d(0, i)
        distance[i] = t
        heap.append((t, i))
    heapify(heap)

    while heap:
        t, i = heappop(heap)
        if vertex[i]:
            continue

        vertex[i] = True
        q += t
        for j in range(n):
            if i == j or vertex[j]:
                continue

            if d(i, j) < distance[j]:
                distance[j] = d(i, j)
                heappush(heap, (distance[j], j))

    print(f'The highest possible quality is 1/{q}.')



# while True:
#     n = int(input())
#     if n == 0:
#         break
#
#     trucks = [input() for _ in range(n)]
#     heap = []
#     for i in range(n):
#         for j in range(i + 1, n):
#             heap.append((sum([trucks[i][k] != trucks[j][k] for k in range(7)]), i, j))
#
#     q = 0
#     heap.sort(reverse=True)
#     edges = [[] for _ in range(n)]
#     count = 0
#     vertex = [False]*n
#     while count < n:
#         d, a, b = heap.pop()
#         edges[a].append(b)
#         edges[b].append(a)
#
#         def dfs(idx, f=None):
#             if f and idx == a:
#                 return False
#
#             for t in edges[idx]:
#                 if t == f:
#                     continue
#
#                 if not dfs(t, idx):
#                     return False
#
#             return True
#
#         if not dfs(a):
#             edges[a].pop()
#             edges[b].pop()
#         else:
#             q += d
#
#             if not vertex[a]:
#                 vertex[a] = True
#                 count += 1
#             if not vertex[b]:
#                 vertex[b] = True
#                 count += 1
#
#     print(f'The highest possible quality is 1/{q}.')
