"""于2024-5-22测试通过"""
import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
datas = [int(i) for i in data[index:index+n]]

ls = [False]*m
fs = [0]
for i in range(1, m + 1):
    fs.append(i**2)
    fs.append(-i**2)

ans = []
for key in datas:
    t = key % m
    for f in fs:
        if ls[(t + f) % m] == False or ls[(t + f) % m] == key:
            ls[(t + f) % m] = key
            ans.append(str((t + f) % m))
            break
print(' '.join(ans))