"""于2024-6-4测试通过"""
s = 65
for idx in range(1, int(input()) + 1):
    print(f'Scenario #{idx}:')
    p, q = map(int, input().split())

    vis = {}

    def dfs(x, y, ans):
        if len(ans) == 2*p*q:
            print(ans)
            return True

        for dx, dy in [(-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < p and 0 <= ny < q:
                key = chr(s + ny) + str(nx + 1)
                if key not in vis or not vis[key]:
                    vis[key] = True
                    if dfs(nx, ny, ans + key):
                        return True
                    vis[key] = False

        return False

    impossible = True

    for i in range(p):
        if not impossible:
            break
        for j in range(q):
            key = chr(s + j) + str(i + 1)
            vis[key] = True
            if dfs(i, j, key):
                impossible = False
                break
            vis[key] = False
    if impossible:
        print('impossible')
    print()
