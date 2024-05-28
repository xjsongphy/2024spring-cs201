"""于2024-5-22测试通过"""
for _ in range(int(input())):
    n, k = map(int, input().split())
    n = str(n)
    for __ in range(k):
        ls = []
        for i in range(len(n)):
            ls.append(int(n[:i] + n[i + 1:]))
        n = str(min(ls))
    print(n)