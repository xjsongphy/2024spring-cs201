"""于2024-5-22测试通过"""
for _ in range(int(input())):
    n, m = map(int, input().split())
    edges = {i: {} for i in range(1, n + 1)}
    for _ in range(m):
        x, y = map(int, input().split())
        edges[x][y] = True
    in_degree = {i: 0 for i in edges}
    for i in edges:
        for j in edges[i]:
            in_degree[j] += 1

    ls = []
    for i in in_degree:
        if in_degree[i] == 0:
            ls.append(i)

    ans = 0
    while ls:
        idx = ls.pop()
        ans += 1
        for i in edges[idx]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                ls.append(i)
    print('No' if ans == n else 'Yes')