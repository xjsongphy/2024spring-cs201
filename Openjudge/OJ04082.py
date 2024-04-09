""""""
n = int(input())
ls = input().split()
idx = 0


def union(a, b):
    if len(a) <= len(b):
        return [a[i] + b[i] for i in range(len(a))] + b[len(a):]
    else:
        return [a[i] + b[i] for i in range(len(b))] + a[len(b):]


class BinaryTree:
    def __init__(self):
        self.value = None
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.father = None
        self.value = None
        self.child = []

    def add(self, tree):
        self.child.append(tree)

    def level(self):
        ans = []
        for tree in self.child:
            ans = union(ans, tree.level())
        return [[self.value]] + ans


def build_binary_tree():
    global idx
    if idx >= len(ls):
        return None
    binary_tree = BinaryTree()
    if ls[idx][0] == '$':
        idx += 1
        return None

    binary_tree.value = ls[idx][0]
    if ls[idx][1] == '1':
        idx += 1
        return binary_tree

    idx += 1
    binary_tree.left = build_binary_tree()
    binary_tree.right = build_binary_tree()
    return binary_tree


def build_tree(binary_tree, father):
    tree = Tree()
    tree.father = father
    if father:
        father.add(tree)
    tree.value = binary_tree.value
    if binary_tree.right:
        build_tree(binary_tree.right, tree.father)
    if binary_tree.left:
        build_tree(binary_tree.left, tree)
    return tree


binary_tree = build_binary_tree()
tree = build_tree(binary_tree, None)
ls = tree.level()
for i in range(len(ls)):
    ls[i].reverse()
    ls[i] = ' '.join(ls[i])
print(' '.join(ls))