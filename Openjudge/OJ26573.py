"""于2024-5-30测试通过"""
n = int(input())
ls = ['*']*(3**n)


def delete(l, r, count):
    t = (r - l + 1) // 3
    nl, nr = l + t, l + 2*t
    for i in range(nl, nr):
        ls[i] = '-'

    if count == 1:
        return
    delete(l, nl - 1, count - 1)
    delete(nr, r, count - 1)


delete(0, 3**n - 1, n)
print(''.join(ls))