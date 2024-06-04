"""于2024-5-28测试通过"""
from copy import copy
while True:
    n, k = map(int, input().split())
    if n == -1:
        break

    matrix = [[[0, 1][s == '#'] for s in input()] for _ in range(n)]
    ans = 0

    def dfs(idx, k, vis):
        if idx == n and k == 0:
            global ans
            ans += 1
            return
        elif idx >= n:
            return

        if k > n - idx + 1:
            return

        dfs(idx + 1, k, copy(vis))
        k -= 1
        for i in range(n):
            if matrix[idx][i] and i not in vis:
                new_vis = copy(vis)
                new_vis[i] = True
                dfs(idx + 1, k, new_vis)

    dfs(0, k, {})
    print(ans)