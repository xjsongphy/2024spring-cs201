"""于2024-6-2测试通过"""
from heapq import *
from math import sqrt

x = y = 0


def dis(x1, y1):
    return sqrt((x - x1)**2 + (y - y1)**2)


sx, sy, fx, fy = map(int, input().split())
v1, v2 = 10*1000/3600, 40*1000/3600
subways = []
while True:
    try:
        s = list(map(int, input().split()))
    except EOFError:
        break

    subways.append([{}, []])
    for i in range(len(s)//2 - 1):
        subways[-1][0][(s[2*i], s[2*i + 1])] = i
        subways[-1][1].append((s[2 * i], s[2 * i + 1]))

vis = {}
heap = [(0.0, sx, sy)]
while True:
    t, x, y = heappop(heap)
    if (fx, fy) == (x, y):
        print(round(t/60))
        exit()

    if (x, y) in vis and vis[(x, y)] <= t:
        continue
    vis[(x, y)] = t

    heappush(heap, (t + dis(fx, fy) / v1, fx, fy))
    for ls in subways:
        for nx, ny in ls[1]:
            nt = t + dis(nx, ny) / v1
            if (nx, ny) in vis and vis[(nx, ny)] <= nt:
                continue
            heappush(heap, (nt, nx, ny))
        if (x, y) not in ls[0]:
            continue
        idx = ls[0][(x, y)]
        if idx > 0:
            nx, ny = ls[1][idx - 1]
            heappush(heap, (t + dis(nx, ny) / v2, nx, ny))
        if idx < len(ls[1]) - 1:
            nx, ny = ls[1][idx + 1]
            heappush(heap, (t + dis(nx, ny) / v2, nx, ny))
