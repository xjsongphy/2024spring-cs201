""""""
class DisjointSet:
    def __init__(self, n):
        self.colas = {i: i for i in range(1, n + 1)}

    def find_root(self, x):
        p = x
        while self.colas[p] != p:
            p = self.colas[p]
        return p

    def equals(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def join(self, x, y):
        root = self.find_root(x)
        p = y
        while self.colas[p] != p:
            t = self.colas[p]
            self.colas[p] = root
            p = t
        self.colas[p] = root

    def not_empty(self):
        bottles = {i: False for i in range(1, len(self.colas) + 1)}
        for i in bottles:
            if self.colas[i] == i:
                bottles[i] = True
        return bottles


while True:
    try:
        n, m = map(int, input().split())
    except EOFError:
        break
    disjoint_set = DisjointSet(n)
    for _ in range(m):
        x, y = map(int, input().split())
        if disjoint_set.equals(x, y):
            print('Yes')
        else:
            print('No')
            disjoint_set.join(x, y)
    bottles = disjoint_set.not_empty()
    ls = []
    for i in bottles:
        if bottles[i]:
            ls.append(str(i))
    print(len(ls))
    print(' '.join(ls))