""""""
from queue import Queue

a, b, c = map(int, input().split())
q = Queue()
q.put(('', 0, 0))
visited = {}

while not q.empty():
    s, i, j = q.get()
    if i == c or j == c:
        print(s.count('\n'), end='')
        print(s)
        exit()
    if (i, j) in visited:
        continue
    visited[(i, j)] = True
    if i < a:
        q.put((s + '\nFILL(1)', a, j))
        if j > 0 and j > a - i:
            q.put((s + '\nPOUR(2,1)', a, j - a + i))
        elif 0 < j <= a - i:
            q.put((s + '\nPOUR(2,1)', i + j, 0))
    if j < b:
        q.put((s + '\nFILL(2)', i, b))
        if i > 0 and i > b - j:
            q.put((s + '\nPOUR(1,2)', i - b + j, b))
        elif 0 < i <= b - j:
            q.put((s + '\nPOUR(1,2)', 0, i + j))
    if i > 0:
        q.put((s + '\nDROP(1)', 0, j))
    if j > 0:
        q.put((s + '\nDROP(2)', i, 0))
print('impossible')
