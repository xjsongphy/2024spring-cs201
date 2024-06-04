n, k = map(int, input().split())
ls = [int(input()) for _ in range(n)]
l, r = 0, max(ls) + 1


def cut(length):
    return sum([t // length for t in ls])


while l < r:
    mid = (l + r) // 2 + 1
    num = cut(mid)

    if num >= k:
        l = mid
    else:
        r = min(mid, r - 1)
print(l)