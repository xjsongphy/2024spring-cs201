"""于2024-5-22测试通过"""
n, m = map(int, input().split())
ls = [int(input()) for _ in range(n)]
l, r = max(ls), sum(ls) + 1


def cost(mid):
    count, temp = 0, 0
    for t in ls:
        temp += t
        if temp > mid:
            temp = t
            count += 1
    if temp > 0:
        count += 1

    return count


while l < r:
    mid = (l + r) // 2
    count = cost(mid)
    if r - l == 1:
        print(l if count <= m else r)
        break
    if count > m:
        l = mid
    else:
        r = mid
    if l == r:
        print(l)
        break