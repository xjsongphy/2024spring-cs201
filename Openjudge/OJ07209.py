""""""
from queue import Queue

m, n = map(int, input().split())
matrix = [input() for _ in range(m)]
vis = {}

sx, sy = 0, 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 'R':
            sx, sy = i, j
            break

q = Queue()
q.put((sx, sy, 0, [f'{sx + 1} {sy + 1}']))
while True:
    x, y, key, way = q.get()
    if matrix[x][y] == 'C' and key:
        print('\n'.join(way))
        exit()
    if (x, y, key) in vis:
        continue
    vis[(x, y, key)] = True
    if matrix[x][y] == 'Y':
        key = 1
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        u, v = x + dx, y + dy
        if 0 <= u < m and 0 <= v < n and matrix[u][v] != '1':
            new_way = way + [f'{u + 1} {v + 1}']
            q.put((u, v, key, new_way))
