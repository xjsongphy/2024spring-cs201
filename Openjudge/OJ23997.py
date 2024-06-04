"""于2024-6-3测试通过"""
from queue import Queue
n = int(input())
q = Queue()

i = 1
id = 0
ans = []
while i <= n:
    q.put((n - i, id, [i]))
    id += 1
    i += 2

while not q.empty():
    t, _, way = q.get()
    if t == 0:
        ans.append(tuple(way))
        continue

    i = way[-1] + 2
    if t < i:
        continue

    while i <= t:
        new_way = way + [i]
        q.put((t - i, id, new_way))
        id += 1
        i += 2

for t in sorted(ans):
    print(' '.join(map(str, t)))
print(len(ans))