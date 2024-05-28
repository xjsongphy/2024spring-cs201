"""于2024-5-28测试通过"""
from copy import copy

sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
others = {}
for _ in range(int(input())):
    x, y = map(int, input().split())
    others[(x, y)] = True

visited = {}
count = 0
shortest_way = None
shortest_length = 0
directions = [(0, 1, -1, 2, 1, 2), (0, -1, -1, -2, 1, -2), (1, 0, 2, 1, 2, -1), (-1, 0, -2, 1, -2, -1)]

queue = {(sx, sy): [1, [f'({sx},{sy})']]}
while True:
    new_queue = {}
    for x, y in queue.keys():
        if (x, y) == (ex, ey):
            count += queue[(x, y)][0]
            shortest_way = queue[(x, y)][1][:]
            continue
        if (x, y) in visited:
            continue
        visited[(x, y)] = True
        to = []
        for x0, y0, x1, y1, x2, y2 in directions:
            if (x + x0, y + y0) in others:
                continue
            to.append((x + x1, y + y1))
            to.append((x + x2, y + y2))
        for nx, ny in to:
            if 0 <= nx <= 10 and 0 <= ny <= 10:
                if (nx, ny) in new_queue:
                    new_queue[(nx, ny)][0] += queue[(x, y)][0]
                    continue
                new_way = queue[(x, y)][1] + [f'({nx},{ny})']
                new_queue[(nx, ny)] = [queue[(x, y)][0], new_way]
    if count > 0:
        break
    queue = copy(new_queue)

if count == 1:
    print('-'.join(shortest_way))
else:
    print(count)
