"""于2024-4-29测试通过"""
import sys
sys.setrecursionlimit(80000)
matrix = [[0]*12]


def fill(i, j):
    matrix[i][j] = 0
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if matrix[i + di][j + dj]:
            fill(i + di, j + dj)


for _ in range(10):
    matrix.append([0] + [[0, 1][i == '.'] for i in list(input())] + [0])
matrix.append([0]*12)

total = 0
for i in range(1, 11):
    for j in range(1, 11):
        if matrix[i][j]:
            fill(i, j)
            total += 1
print(total)