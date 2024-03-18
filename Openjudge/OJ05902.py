"""于2024-3-12测试通过"""


class Node:
    def __init__(self, value):
        self.pre = None
        self.next = None
        self.value = value


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def insort(self, value):
        if self.head:
            now_tail = self.tail
            new_tail = Node(value)
            self.tail = now_tail.next = new_tail
            new_tail.pre = now_tail
        else:
            self.head = self.tail = Node(value)

    def pop(self, c):
        if not self.head:
            return

        if c:
            self.tail = self.tail.pre
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            self.head = self.head.next
            if self.head:
                self.head.pre = None
            else:
                self.tail = None

    def __str__(self):
        if not self.head:
            return 'NULL'

        s = [str(self.head.value)]
        t = self.head
        while t.next:
            t = t.next
            s.append(str(t.value))

        return ' '.join(s)


for i in range(int(input())):
    queue = Queue()
    for j in range(int(input())):
        t, c = map(int, input().split())
        if t == 1:
            queue.insort(c)
        else:
            queue.pop(c)
    print(queue)