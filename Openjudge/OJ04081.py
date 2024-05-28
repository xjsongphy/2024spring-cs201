""""""
class Tree:
    def __init__(self):
        self.value = self.parent = None
        self.child = []

    def add(self):
        child = Tree()
        child.parent = self
        child.value = True
        self.child.append(child)

        return child

    def height(self):
        if self.value:
            if self.child:
                return 1 + max([child.height() for child in self.child])
            return 1
        return 0

    def build(self, tree):
        if not tree.value:
            return
        self.value = True
        son = self
        for child in tree.child:
            right = Tree()
            right.parent = son
            son.child.append(right)
            right.build(child)
            son = right


s = input()
raw = Tree()
p = raw
p.value = True
for c in s:
    if c == 'd':
        p = p.add()
    else:
        p = p.parent
new = Tree()
new.build(raw)
print(f'{raw.height() - 1} => {new.height() - 1}')

