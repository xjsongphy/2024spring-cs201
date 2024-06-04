"""于2024-5-30测试通过"""
ls, idx = [], 0


class BinaryTree:
    def __init__(self):
        self.v = None
        self.l = self.r = None

    def build(self):
        global idx
        root_idx = idx
        self.v = ls[idx][-1]
        idx += 1
        self.l = BinaryTree()
        self.r = BinaryTree()
        if self.v == '*':
            return
        if idx == len(ls):
            return

        if len(ls[idx]) == len(ls[root_idx]) + 1:
            self.l.build()
            if idx == len(ls):
                return
        if len(ls[idx]) == len(ls[root_idx]) + 1:
            self.r.build()

    def front(self):
        if not self.v or self.v == '*':
            return ''
        return self.v + self.l.front() + self.r.front()

    def mid(self):
        if not self.v or self.v == '*':
            return ''
        return self.l.mid() + self.v + self.r.mid()

    def back(self):
        if not self.v or self.v == '*':
            return ''
        return self.l.back() + self.r.back() + self.v


for _ in range(int(input())):
    ls = []
    while True:
        t = input()
        if t == '0':
            break
        ls.append(t)

    idx = 0
    tree = BinaryTree()
    tree.build()
    print(tree.front())
    print(tree.back())
    print(tree.mid())
    print()