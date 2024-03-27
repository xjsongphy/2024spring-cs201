"""于2024-3-19测试通过"""


class BinarySearchTree:
    def __init__(self, value = None):
        self.value = value
        self.left = self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = BinarySearchTree(value)
            else:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BinarySearchTree(value)
        else:
            self.value = value

    def iterate(self):
        if not self.value:
            return []

        result = []
        if self.left:
            result = self.left.iterate()
        if self.right:
            right = self.right.iterate()
            for i in range(min(len(result), len(right))):
                result[i] = ' '.join([result[i], right[i]])
            result += right[len(result):]
        return [f'{self.value}'] + result


tree = BinarySearchTree()
dic = {}
for i in input().split():
    if i in dic:
        continue
    tree.insert(int(i))
    dic[i] = True
print(' '.join(tree.iterate()))
