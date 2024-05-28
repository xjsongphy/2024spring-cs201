"""于2024-5-28测试通过"""
from queue import Queue
from copy import copy

n = int(input())


def judge(x):
    return 0 <= x < n


matrix = [[int(s) for s in input()] for _ in range(n)]
visited = {}
q = Queue()
for x in range(n):
    for y in range(n):
        if matrix[x][y] == 1:
            q.put((x, y))
            break
    if not q.empty():
        break

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while not q.empty():
    x, y = q.get()
    if (x, y) in visited:
        continue
    visited[(x, y)] = True
    for dx, dy in directions:
        u, v = x + dx, y + dy
        if judge(u) and judge(v) and matrix[u][v]:
            q.put((u, v))

l = 0
q = copy(visited)
root = copy(visited)
visited = {}
while True:
    new_q = {}
    for x, y in q.keys():
        if (x, y) in visited:
            continue
        visited[(x, y)] = True
        if matrix[x][y] and (x, y) not in root:
            print(l - 1)
            exit()
        for dx, dy in directions:
            u, v = x + dx, y + dy
            if judge(u) and judge(v):
                new_q[(u, v)] = True
    l += 1
    q = copy(new_q)