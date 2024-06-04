"""于2024-6-4测试通过"""
from math import log2


def father(x):
    return (x + 1) // 2 - 1


k, n = map(int, input().split())
ls = [[0, 0] for _ in range((1 << k) - 1)]
h = [int(log2(x + 1)) for x in range((1 << k) - 1)]

for _ in range(n):
    s = list(map(int, input().split()))
    x = s[1] - 1
    if len(s) == 3:
        y = s[2]
        ls[x][1] += y
        p = father(x)
        cnt = (1 << (k - h[x])) - 1
        while p >= 0:
            ls[p][0] += y * cnt
            p = father(p)
        continue

    p = x
    cnt = (1 << (k - h[x])) - 1
    ans = 0
    while p >= 0:
        ans += ls[p][1]*cnt
        p = father(p)
    print(ans + ls[x][0])
