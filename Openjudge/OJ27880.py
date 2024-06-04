"""于2024-5-28测试通过"""
from heapq import *

n, m = map(int, input().split())
roads = {i: {} for i in range(1, n + 1)}
for _ in range(m):
    u, v, c = map(int, input().split())
    roads[u][v] = roads[v][u] = c

choices = {i: {} for i in range(1, n + 1)}
crosses = [1]
heap = []
in_heap = {}
max_cost = 0
visited = {}


def loop(idx, f=None):
    if idx in visited:
        return True

    visited[idx] = True
    for to in choices[idx]:
        if to != f:
            if loop(to, idx):
                return True

    return False


for _ in range(n - 1):
    idx = crosses[-1]
    for to, c in roads[idx].items():
        if (idx, to) not in in_heap and (to, idx) not in in_heap:
            heappush(heap, (c, idx, to))
            in_heap[(idx, to)] = True

    while True:
        c, u, v = heappop(heap)
        choices[u][v] = choices[v][u] = True
        visited = {}
        if loop(u):
            del choices[u][v]
            del choices[v][u]
        else:
            max_cost = max(max_cost, c)
            crosses.append(v)
            break
print(n - 1, max_cost)