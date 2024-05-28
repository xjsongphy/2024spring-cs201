"""于2024-5-21测试通过"""
import sys

input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
ls = [int(i) for i in data[index:index+n]]

dic = [-1]*m
ans = []
for key in ls:
    t = key % m
    for d in range(m):
        real_key = (t + d) % m
        if dic[real_key] == -1 or dic[real_key] == key:
            dic[real_key] = key
            ans.append(str(real_key))
            break
print(' '.join(ans))
