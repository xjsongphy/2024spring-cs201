"""于2024-4-28测试通过"""
def main(ls):
    l = len(ls)
    if l == 8:
        return [ls]
    ans = []
    for i in range(1, 9):
        available = True
        for j in range(l):
            if ls[j] == i or (abs(ls[j] - i) == l - j):
                available = False
        if available:
            t = ls + [i]
            for u in main(t):
                ans.append(u)

    return ans


ans = main([])
for _ in range(int(input())):
    print(''.join(map(str, ans[int(input()) - 1])))