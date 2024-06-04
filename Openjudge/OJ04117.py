"""于2024-6-4测试通过"""
dp = {}


def dfs(n, m):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif m == 0:
        return 0

    if (n, m) in dp:
        return dp[(n, m)]
    ans = 0
    for i in range(m, -1, -1):
        ans += dfs(n - i, min(i, m))
    dp[(n, m)] = ans
    return ans


while True:
    try:
        n = int(input())
    except EOFError:
        break
    print(dfs(n, n))