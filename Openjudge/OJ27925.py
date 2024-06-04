"""于2024-6-4测试通过"""
from queue import Queue

t = int(input())
groups = {}
search = {}
for i in range(t):
    ls = input().split()
    groups[i] = ls
    for j in ls:
        search[j] = i
q = []
start = 0
l = 0
groups_in = {i: -1 for i in range(t)}

while True:
    s = input().split()
    if s[0][0] == 'S':
        break
    elif s[0][0] == 'D':
        print(q[start].get())
        if q[start].empty():
            start += 1
            l -= 1
    else:
        num = s[1]
        if num not in search:
            search[num] = num
            groups[num] = [num]
            groups_in[num] = -1
        idx = search[num]
        i = groups_in[idx]
        if i >= start:
            q[i].put(num)
        else:
            groups_in[idx] = start + l
            q.append(Queue())
            q[-1].put(num)
            l += 1