"""于2024-4-9测试通过"""
n, m = map(int, input().split())
edges = {i: [] for i in range(n)}
values = list(map(int, input().split()))

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

ans = 0


def dfs(idx, visited):
    visited[idx] = True
    value = values[idx]
    for i in edges[idx]:
        if visited[i]:
            continue
        value += dfs(i, visited)
    return value


for i in range(n):
    ans = max(ans, dfs(i, [False] * n))
print(ans)