"""于2024-4-17测试通过"""
from queue import Queue

n = int(input())
ls = [input() for _ in range(n)]
start, end = input().split()

ls = [start, end] + ls
ls = list({s: None for s in ls}.keys())
n = len(ls)
q = Queue()

edges = {i: {} for i in range(n)}
parts = {}
for i in range(n):
    s = ls[i]
    for j in range(4):
        t = s[:j] + '_' + s[j + 1:]
        if t in parts:
            parts[t][i] = True
        else:
            parts[t] = {i: True}

for d in parts.values():
    t = list(d)
    l = len(t)
    for i in range(l):
        for j in range(i + 1, l):
            edges[t[i]][t[j]] = True
            edges[t[j]][t[i]] = True

q.put([0])
visited = [False for i in range(n)]

while not q.empty():
    way = q.get()
    idx = way[-1]
    s = ls[idx]

    if idx == 1:
        print(' '.join([ls[i] for i in way]))
        exit()

    if visited[idx]:
        continue

    visited[idx] = True
    for j in edges[idx]:
        if not visited[j]:
            q.put(way + [j])
print('NO')