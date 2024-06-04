"""于2024-6-4测试通过"""
from queue import Queue

s = input()
values = {}
for _ in range(int(input())):
    a, b = input().split()
    values[a] = int(b)

ans = []
op = []
operators = {'+': 1, '-': 1, '*': 2, '/': 2}
words = {i: True for i in 'abcdefghijklmnopqrstuvwxyz'}

idx = 0
n = len(s)
while idx < n:
    if s[idx] in words:
        ans.append(s[idx])
    elif s[idx] == '(':
        op.append('(')
    elif s[idx] == ')':
        while op[-1] != '(':
            ans.append(op.pop())
        op.pop()
    else:
        while op and op[-1] != '(' and operators[op[-1]] >= operators[s[idx]]:
            ans.append(op.pop())
        op.append(s[idx])
    idx += 1
op.reverse()
ans += op
print(''.join(ans))
idx = 0


class Tree:
    def __init__(self):
        self.l = self.r = self.v = self.h = self.x = self.father = None

    def get_height(self):
        h = self.l.get_height() if self.l else 0
        if self.r:
            h = max(h, self.r.get_height())

        h += 1
        self.h = h
        return h

    def fill(self, h):
        if h == 1:
            return

        if not self.l:
            self.l = Tree()
            self.l.father = self
        if not self.r:
            self.r = Tree()
            self.r.father = self
        self.l.fill(h - 1)
        self.r.fill(h - 1)


tree_stack = []
num_stack = []
for c in ans:
    tree = Tree()
    tree.v = c
    if c in words:
        tree_stack.append(tree)
        num_stack.append(values[c])
    else:
        tree.r = tree_stack.pop()
        tree.l = tree_stack.pop()
        tree.r.father = tree.l.father = tree
        tree_stack.append(tree)

        b = num_stack.pop()
        a = num_stack.pop()
        num_stack.append([a + b, a - b, a*b][['+', '-', '*'].index(c)] if c != '/' else a//b)

tree = tree_stack[0]
tree.get_height()
tree.fill(tree.h)
ans = num_stack[0]

q = Queue()
q.put(tree)
leaves = []
while not q.empty():
    t = q.get()
    if t.l:
        q.put(t.l)
        q.put(t.r)
    else:
        leaves.append(t)

length = 2**tree.h - 1
visualize = []
new_leaves = []
idx = 0
while leaves:
    visualize.append([' '] * length)
    visualize.append([' '] * length)
    for leaf in leaves:
        if leaf.l:
            leaf.x = (leaf.l.x + leaf.r.x) // 2
        else:
            leaf.x = idx
            idx += 2

        if leaf.v:
            visualize[-1][leaf.x] = leaf.v
        if leaf.l and leaf.l.v:
            visualize[-2][leaf.x - 1] = '/'
        if leaf.r and leaf.r.v:
            visualize[-2][leaf.x + 1] = '\\'

        if leaf.father and leaf.father.l == leaf:
            new_leaves.append(leaf.father)

    leaves = new_leaves[:]
    new_leaves = []

visualize.reverse()
visualize.pop()
print('\n'.join([''.join(t) for t in visualize]))
print(ans)