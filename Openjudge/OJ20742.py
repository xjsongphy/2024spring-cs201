"""于2024-2-19测试通过"""
ls = [0, 1, 1]
for i in range(30):
    ls.append(ls[-1] + ls[-2] + ls[-3])
print(ls[int(input())])