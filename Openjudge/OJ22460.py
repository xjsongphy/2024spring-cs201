"""于2024-6-3测试通过"""
ls = []
idx = 0
length = 0


class Tree:
    def __init__(self):
        self.l = self.r = None

    def build(self):
        global idx

        if idx == length - 1:
            idx += 1
            return ls[idx - 1] == '#'

        if ls[idx] == '#':
            idx += 1
            return True
        idx += 1
        self.l = Tree()
        if self.l.build():
            if idx == length:
                return False

            self.r = Tree()
            return self.r.build()
        return False


while True:
    n = int(input())
    idx = 0
    if n == 0:
        break

    ls = input().split()
    length = len(ls)
    tree = Tree()
    print('T' if (tree.build() and idx == len(ls)) else 'F')