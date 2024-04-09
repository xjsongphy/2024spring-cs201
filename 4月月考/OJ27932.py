"""于2024-4-3测试通过"""
n, k = map(int, input().split())
ls = sorted(list(map(int, input().split())))
if k == n:
    print(ls[-1])
elif k == 0:
    print(1 if ls[0] != 1 else -1)
else:
    print(ls[k - 1] if ls[k - 1] != ls[k] else -1)