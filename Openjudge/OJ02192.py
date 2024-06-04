"""于2024-5-28测试通过"""
found = False
for idx in range(1, int(input()) + 1):
    vis = {}
    a, b, c = input().split()
    found = False

    def dfs(i, j, k):
        if (i, j, k) in vis:
            return
        vis[(i, j, k)] = True
        global found
        if found:
            return
        if k == len(c):
            found = True
            return
        if i < len(a) and c[k] == a[i]:
            dfs(i + 1, j, k + 1)
        if j < len(b) and c[k] == b[j]:
            dfs(i, j + 1, k + 1)

    dfs(0, 0, 0)
    print(f'Data set {idx}: {["no", "yes"][found]}')