n = int(input())
matrix = [[0]*(n + 1) for _ in range(n + 1)]

count = 0
i, j = 1, 1
while count < n*n:
    ls = input().split()
    if not ls:
        continue

    ls = list(map(int, ls))
    count += len(ls)
    for k in ls:
        matrix[i][j] = matrix[i][j - 1] + k
        j += 1
        if j == n + 1:
            j = 1
            i += 1

for i in range(1, n + 1):
    for j in range(n + 1):
        matrix[i][j] += matrix[i - 1][j]

ans = -float('inf')

for i in range(n):
    for j in range(n):
        for k in range(j + 1, n + 1):
            ans = max(ans, max([matrix[l][k] - matrix[l][j] - matrix[i][k] + matrix[i][j] for l in range(i + 1, n + 1)]))
print(ans)