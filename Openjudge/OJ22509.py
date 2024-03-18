"""于2024-3-16测试通过"""
from math import log2

y = 0


def f(x):
    return x * x + x + 1 + log2(x) - y


while True:
    try:
        y = int(input())
    except EOFError:
        break
    l, r = 0, y
    while r - l > 1e-5:
        mid = (l + r) / 2
        if f(mid) > 0:
            r = mid
        else:
            l = mid
    print("%.4f" % l)