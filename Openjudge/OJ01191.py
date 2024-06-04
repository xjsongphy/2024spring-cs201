"""于2024-6-4测试通过"""
def f(n, x1, y1, x2, y2):
    if (n, x1, y1, x2, y2) in dp:
        return dp[(n, x1, y1, x2, y2)]
    if n == 1:
        su = 0
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                su += l[i][j]
        dp[(n, x1, y1, x2, y2)] = su*su
        return su*su

    mi = float('inf')
    for i in range(x1, x2):
        mi = min(mi, f(n - 1, x1, y1, i, y2) + f(1, i + 1, y1, x2, y2))
        mi = min(mi, f(1, x1, y1, i, y2) + f(n - 1, i + 1, y1, x2, y2))
    for i in range(y1, y2):
        mi = min(mi, f(n - 1, x1, y1, x2, i) + f(1, x1, i + 1, x2, y2))
        mi = min(mi, f(1, x1, y1, x2, i) + f(n - 1, x1, i + 1, x2, y2))
    dp[(n, x1, y1, x2, y2)] = mi
    return mi


n = int(input())
l = [list(map(int, input().split())) for _ in range(8)]
dp = {}

print("%.3f" % (f(n, 0,0,7,7)/n-sum([sum(t) for t in l])**2/n**2)**0.5)