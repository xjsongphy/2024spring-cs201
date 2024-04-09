"""于2024-4-3测试通过"""
from queue import Queue

m, n = map(int, input().split())
q = Queue()
l = ans = 0
dic = {}
for s in input().split():
    if s not in dic or not dic[s]:
        ans += 1
        dic[s] = True
        q.put(s)
        l += 1
    if l > m:
        t = q.get()
        dic[t] = False
        l -= 1
print(ans)
