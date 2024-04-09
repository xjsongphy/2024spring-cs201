"""于2024-4-3测试通过"""
dic = {}
n = int(input())
for _ in range(n):
    ls = list(map(int, input().split()))
    dic[ls[0]] = ls[1:]
roots = {i: True for i in dic}
for i in dic:
    for j in dic[i]:
        roots[j] = False
for i in roots:
    if roots[i]:
        root = i
        break


def iterate(i):
    ls = sorted([i] + dic[i])
    for j in ls:
        if i == j:
            print(i)
        else:
            iterate(j)


iterate(root)