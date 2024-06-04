"""于2024-6-4测试通过"""
from queue import Queue

ls = []


class Tree:
    def __init__(self):
        self.v = None
        self.degree = None
        self.kids = []

    def build(self):
        q = Queue()
        q.put(self)
        idx = 0

        while not q.empty():
            p = q.get()
            p.v = ls[idx]
            idx += 1
            p.degree = int(ls[idx])
            idx += 1
            for _ in range(p.degree):
                p.kids.append(Tree())
                q.put(p.kids[-1])

    def back(self):
        ans = []
        for tree in self.kids:
            ans += tree.back()

        return ans + [self.v]


ans = []
for _ in range(int(input())):
    ls = input().split()
    tree = Tree()
    tree.build()
    ans += tree.back()
print(' '.join(ans))