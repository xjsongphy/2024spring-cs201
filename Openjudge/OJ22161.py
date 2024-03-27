class Node:
    def __init__(self):
        self.w = 0
        self.char = None
        self.left = self.right = None
        self.min_char = None


class Huffman:
    def __init__(self):
        self.root = None
        self.code = {}

    def coding(self, node=None, pre = ''):
        if node is None:
            node = self.root

        if node.char:
            self.code[node.char] = pre
            return
        else:
            self.coding(node.left, pre + '0')
            self.coding(node.right, pre + '1')

    def encoding(self, data):
        ans = ''
        for s in data:
            ans += self.code[s]
        return ans

    def decoding(self, data, i=0):
        if i >= len(data):
            return ''

        p = self.root
        while True:
            if p.char:
                return p.char + self.decoding(data, i)
            else:
                p = [p.left, p.right][data[i] == '1']
            i += 1

    def building(self, ls):
        nodes = []
        for c, w in ls:
            node = Node()
            node.char = node.min_char = c
            node.w = w
            nodes.append(node)

        for _ in range(len(ls) - 1):
            nodes.sort(key=lambda t: (t.w, t.min_char), reverse=True)
            l, r = nodes.pop(), nodes.pop()
            new_node = Node()
            new_node.left = l
            new_node.right = r
            new_node.w = l.w + r.w
            new_node.min_char = min(l.min_char, r.min_char)
            nodes.append(new_node)

        self.root = nodes[0]
        self.coding()


tree = Huffman()
ls = []
for _ in range(int(input())):
    c, w = input().split()
    ls.append((c, int(w)))
tree.building(ls)

while True:
    try:
        s = input()
    except EOFError:
        break
    if s[0] == '0' or s[0] == '1':
        print(tree.decoding(s))
    else:
        print(tree.encoding(s))