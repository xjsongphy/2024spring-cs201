"""于2024-3-6测试通过"""
while True:
    n = int(input())
    if not n:
        break
    item_dic = {}
    for h in [tuple(map(int, input().split())) for _ in range(n)]:
        if h in item_dic:
            item_dic[h] += 1
        else:
            item_dic[h] = 1

    dist_dic = {}
    cost_dic = {}

    dist_ls = sorted(list(item_dic.keys()), key=lambda t: t[0])
    cost_ls = sorted(list(item_dic.keys()), key=lambda t: t[1])
    ans = 0

    t = float('inf')
    for h in dist_ls:
        if h[0] not in dist_dic:
            dist_dic[h[0]] = t
        t = min(t, h[1])
    t = float('inf')
    for h in cost_ls:
        if h[1] not in cost_dic:
            cost_dic[h[1]] = t
        t = min(t, h[0])

    for h in item_dic:
        if h[0] < cost_dic[h[1]] and h[1] < dist_dic[h[0]]:
            ans += item_dic[h]
    print(ans)
