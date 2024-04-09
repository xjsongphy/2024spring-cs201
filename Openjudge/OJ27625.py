"""于2024-4-3测试通过"""
n = int(input())
ls = [0, 1, 2]
for _ in range(n - 2):
    ls.append(ls[-1] + ls[-2] + 1)
print(ls[n])