""""""
class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.parent = None
        self.bal = 0

    def has_left(self):
        return self.left

    def has_right(self):
        return self.right

    def is_left(self):
        return self.parent and (self.parent.lelf == self)

    def is_right(self):
        return self.parent and (self.parent.right == self)

    def insert(self, value):
        if value > self.value:
            if self.has_right():
                h = self.right.insert(value)
                self.bal += h
                return h if h * (self.bal - h) >= 0 else 0
            else:
                self.right = Node()
                self.right.value = value
                self.bal -= 1
                return 0 if self.has_left() else -1
        else:
            if self.has_left():
                h = self.left.insert(value)
                self.bal += h
                return h if h * (self.bal - h) >= 0 else 0
            else:
                self.left = Node()
                self.left.value = value
                self.bal += 1
                return 0 if self.has_right() else 1

    def left_rotate(self):

    def right_rotate(self):
class AVL:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = Node()
            self.root.value = value