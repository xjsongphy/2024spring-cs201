"""于2024-3-5测试通过"""
n = int(input())
ds = []
for i in range(4):
    ds.append(set(list(input())))
ls = ['']
l = 1
dic = {'': True}
for i in range(4):
    rl = l
    for j in ds[i]:
        for k in range(rl):
            key = ''.join(sorted(ls[k] + j))
            if key in dic:
                continue
            dic[key] = True
            l += 1
            ls.append(key)
for _ in range(n):
    print('YES' if ''.join(sorted(input())) in dic else 'NO')