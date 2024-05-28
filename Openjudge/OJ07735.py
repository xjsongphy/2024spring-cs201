"""于2024-5-23测试通过"""
from heapq import *

k, n, r = int(input()), int(input()), int(input())
roads = {i: {} for i in range(1, n + 1)}
for _ in range(r):
    s, d, l, t = map(int, input().split())
    if d not in roads[s]:
        roads[s][d] = []
    roads[s][d].append((l, t))

heap = [(0, 1, k)]
vis = {}
while heap:
    s, idx, coins = heappop(heap)
    if idx == n:
        print(s)
        exit()
    if idx not in vis:
        vis[idx] = (s, coins)
    else:
        if vis[idx][0] <= s and vis[idx][1] >= coins:
            continue
        elif vis[idx][0] > s and vis[idx][1] < coins:
            vis[idx] = (s, coins)
    for d in roads[idx]:
        for l, t in roads[idx][d]:
            if t <= coins:
                heappush(heap, (s + l, d, coins - t))
print(-1)