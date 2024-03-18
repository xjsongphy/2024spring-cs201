"""于2024-3-18测试通过"""
s = ''
idx = 0


class Tree:
    def __init__(self):
        self.value = self.left_tree = self.right_tree = None

    def layers(self):
        ans = []

        if self.left_tree:
            ans = self.left_tree.layers()
        if self.right_tree:
            t = self.right_tree.layers()
            for i in range(min(len(t), len(ans))):
                ans[i] += t[i]
            ans += t[len(ans):]

        return [self.value] + ans

    def initializing(self):
        global s, idx
        self.value = s[idx]
        if s[idx].islower():
            idx -= 1
            return

        idx -= 1
        self.right_tree = Tree()
        self.right_tree.initializing()
        self.left_tree = Tree()
        self.left_tree.initializing()

        return


for _ in range(int(input())):
    s = input()
    idx = len(s) - 1
    tree = Tree()
    tree.initializing()
    ans = ''.join(tree.layers())
    print(''.join([ans[i] for i in range(len(ans) - 1, -1, -1)]))
