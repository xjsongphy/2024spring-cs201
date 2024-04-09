"""于2024-4-3测试通过"""
def s_type(s):
    if '1' not in s:
        return 'B'
    elif '0' not in s:
        return 'I'
    else:
        return 'F'


class Tree:
    def __init__(self):
        self.t = ''
        self.left = self.right = None

    def build_tree(self, s):
        self.t = s_type(s)

        if len(s) == 1:
            return
        else:
            mid = len(s) // 2
            self.left = Tree()
            self.right = Tree()
            self.left.build_tree(s[:mid])
            self.right.build_tree(s[mid:])

    def __str__(self):
        if self.left:
            return str(self.left) + str(self.right) + self.t
        else:
            return self.t


input()
s = input()
tree = Tree()
tree.build_tree(s)
print(tree)