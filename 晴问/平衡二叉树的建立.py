"""于2024-3-27测试通过"""
class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.bal = 0

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def insert(self, value):
        if value > self.value:
            if self.has_right():
                h = self.right.insert(value)
                h = 0 if h == 0 else -1
            else:
                self.right = Node()
                self.right.value = value
                h = -1
        else:
            if self.has_left():
                h = self.left.insert(value)
                h = 0 if h == 0 else 1
            else:
                self.left = Node()
                self.left.value = value
                h = 1
        self.bal += h
        if abs(self.bal) == 2:
            self.adjust()
            return 0
        return h if h * (self.bal - h) >= 0 else 0

    def left_rotate(self):
        bal_self = max(self.bal + 1, self.right.bal) + 1
        bal_left = self.bal + 1 - min(0, self.right.bal)

        new = Node()
        new.value = self.value
        new.right = self.right.left
        new.left = self.left
        new.bal = bal_left

        self.left = new
        self.value = self.right.value
        self.right = self.right.right
        self.bal = bal_self

    def right_rotate(self):
        bal_self = min(self.bal - 1, self.left.bal) - 1
        bal_right = self.bal - 1 - max(0, self.left.bal)

        new = Node()
        new.value = self.value
        new.left = self.left.right
        new.right = self.right
        new.bal = bal_right

        self.right = new
        self.value = self.left.value
        self.left = self.left.left
        self.bal = bal_self

    def front(self):
        ans = [self.value]
        ans += self.left.front() if self.has_left() else []
        ans += self.right.front() if self.has_right() else []
        return ans

    def adjust(self):
        if self.bal < 0:
            if self.has_right() and self.right.bal > 0:
                self.right.right_rotate()
            self.left_rotate()
        else:
            if self.has_left() and self.left.bal < 0:
                self.left.left_rotate()
            self.right_rotate()


class AVL:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = Node()
            self.root.value = value

    def front(self):
        if self.root:
            return self.root.front()
        return []


avl = AVL()
input()
for i in map(int, input().split()):
    avl.insert(i)
print(' '.join(map(str, avl.front())))