"""于2024-2-19测试通过"""
ls = list(map(int, input().split()))
dic = {i: 0 for i in set(ls)}
for i in ls:
    dic[i] += 1

ls = sorted([(-v, k) for k, v in dic.items()])
c = ls[0][0]
print(ls[0][1], end='')
for i in ls[1:]:
    if i[0] > c:
        break
    print(f' {i[1]}', end='')