"""于2024-3-6测试通过"""


def mid_num(ls):
    n = len(ls)
    if n % 2 == 0:
        return (ls[n // 2 - 1] + ls[n // 2]) / 2
    return ls[n // 2]


dist_ls = []
n = int(input())
for s in input().split():
    x, y = map(int, s[1: -1].split(','))
    dist_ls.append(x + y)
price_ls = list(map(int, input().split()))
dist_per_price_ls = [dist_ls[i] / price_ls[i] for i in range(n)]
ls = [(dist_per_price_ls[i], price_ls[i]) for i in range(n)]

mid_dist_per_price = mid_num(sorted(dist_per_price_ls))
mid_price = mid_num(sorted(price_ls))
print(sum([[0, 1][ls[i][0] > mid_dist_per_price and ls[i][1] < mid_price] for i in range(n)]))