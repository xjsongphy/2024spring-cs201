"""于2024-4-28测试通过"""
from heapq import *
for _ in range(int(input())):
    n, m = map(int, input().split())
    matrix = ['#'*(m + 2)] + ['#' + input() + '#' for __ in range(n)] + ['#'*(m + 2)]
    r, s = 0, 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if matrix[i][j] == 'r':
                heap = [(0, i, j)]
                break
    heapify(heap)
    visited = {}
    ans = False
    while heap:
        t, i, j = heappop(heap)
        if (i, j) in visited and visited[(i, j)] <= t:
            continue
        if matrix[i][j] == 'a':
            ans = t
            break
        visited[(i, j)] = t
        t += 1 + (matrix[i][j] == 'x')
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = i + dx, j + dy
            if (x, y) in visited and visited[(x, y)] <= t:
                continue
            if matrix[x][y] == '#':
                continue
            heappush(heap, (t, x, y))
    print(ans if ans else 'Impossible')
