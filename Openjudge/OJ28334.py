"""于2024-5-29测试通过"""
n, m = map(int, input().split())
edges = {i: {} for i in range(n)}
for _ in range(m):
    a, b = map(int, input().split())
    edges[a][b] = True

count = 0


def loop():
    num = 0
    in_degree = {i: 0 for i in range(n)}
    stack = []

    for i in range(n):
        for j in edges[i]:
            in_degree[j] += 1
    for i in range(n):
        if in_degree[i] == 0:
            stack.append(i)

    while stack:
        num += 1
        idx = stack.pop()
        for i in edges[idx]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                stack.append(i)

    return not num == n


for i in range(n):
    for j in range(n):
        if i == j or j in edges[i]:
            continue
        edges[i][j] = True
        if not loop():
            count += 1
        else:
            del edges[i][j]
print(count)