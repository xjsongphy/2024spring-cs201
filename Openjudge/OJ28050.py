"""于2024-4-20测试通过"""
from copy import copy
from heapq import *

direction = [(2, 1), (1, 2), (2, -1), (-1, 2), (-2, 1), (1, -2), (-2, -1), (-1, -2)]
n = int(input())
sr, sc = map(int, input().split())


def dfs(x, y, l, visited):
    visited[(x, y)] = True
    l += 1

    if l == n*n:
        print('success')
        exit()

    heap = []
    for dx, dy in direction:
        x1, y1 = x + dx, y + dy
        if 0 <= x1 < n and 0 <= y1 < n:
            if (x1, y1) in visited:
                continue
            t = 0
            for dx1, dy1 in direction:
                x2, y2 = x1 + dx1, y1 + dy1
                if 0 <= x2 < n and 0 <= y2 < n:
                    t += (x2, y2) not in visited
            heap.append((t, x1, y1))
    heapify(heap)
    while heap:
        t, x1, y1 = heappop(heap)
        dfs(x1, y1, l, copy(visited))


dfs(sr, sc, 0, {})
print('fail')