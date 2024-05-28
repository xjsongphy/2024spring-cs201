"""于2024-5-23测试通过"""
from heapq import *

n, p, k = map(int, input().split())
edges = {i: {} for i in range(1, n + 1)}
r = 0
for _ in range(p):
    a, b, l = map(int, input().split())
    edges[a][b] = edges[b][a] = l
    r = max(r, l)
r += 1
raw_r = r


def search(lim):
    heap = [(-1, -k)]
    heapify(heap)
    vis = {}
    while heap:
        idx, free = heappop(heap)
        idx, free = -idx, -free
        if idx == n:
            return 1
        if idx not in vis or vis[idx] < free:
            vis[idx] = free
        else:
            continue

        for t, l in edges[idx].items():
            new_free = free
            if l > lim:
                if new_free > 0:
                    new_free -= 1
                else:
                    continue
            if t in vis and vis[t] >= new_free:
                continue
            heappush(heap, (-t, -new_free))
    return 0


l = 0
while l < r:
    if l + 1 == r:
        ans_l = search(l)
        ans_r = search(r)
        if ans_l == ans_r == 0:
            print(-1)
        else:
            print(l if ans_l else r)
        exit()
    mid = (l + r) // 2
    ans = search(mid)
    if ans == 0:
        l = mid
        continue
    r = mid
print(l)