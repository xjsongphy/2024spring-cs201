"""于2024-3-5测试通过"""
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    ls = list(range(1, n + 1))
    idx = 0
    for i in range(n - 1):
        idx = (idx + m - 1) % (n - i)
        ls.pop(idx)
        if idx == n - i - 1:
            idx = 0
    print(ls[0])