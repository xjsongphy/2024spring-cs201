"""于2024-3-11测试通过"""
ls = []


def merge_sort(i, j):
    if j <= i:
        return 0
    mid = (i + j) >> 1
    t = merge_sort(i, mid) + merge_sort(mid + 1, j)

    temp = ls[i: j + 1]
    mid -= i
    l, r = 0, mid + 1
    for idx in range(i, j + 1):
        if l > mid:
            ls[idx] = temp[r]
            r += 1
        elif r > j - i:
            ls[idx] = temp[l]
            l += 1
        elif temp[l] <= temp[r]:
            ls[idx] = temp[l]
            l += 1
        else:
            ls[idx] = temp[r]
            r += 1
            t += mid - l + 1

    return t


while True:
    n = int(input())
    if not n:
        break
    ls = [int(input()) for _ in range(n)]
    print(merge_sort(0, n - 1))

# output = ''
# while True:
#     ans = 0
#     n = int(input())
#     if not n:
#         break
#
#     ls = sorted([(int(input()), i + 1) for i in range(n)])
#     ls = [i[1] for i in ls]
#
#     tr = [0] * (n + 1)
#     for i in range(1, n + 1):
#         while i <= n:
#             tr[i] += 1
#             i += i & -i
#
#     for idx in ls:
#         j = idx
#         while j <= n:
#             tr[j] += -1
#             j += j & -j
#
#         x = 0
#         y = idx - 1
#
#         while y > x:
#             ans += tr[y]
#             y -= y & -y
#         while x > y:
#             ans -= tr[x]
#             x -= x & -x
#
#     print(ans)
