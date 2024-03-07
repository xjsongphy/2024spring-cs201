"""于2024-3-6测试通过"""
while True:
    n, idx, m = map(int, input().split())
    if not n:
        break
    idx -= 1
    ans = []
    ls = list(range(1, n + 1))
    for i in range(n):
        idx = (idx + m - 1) % (n - i)
        ans.append(str(ls[idx]))
        ls.pop(idx)
    print(','.join(ans))
