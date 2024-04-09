"""于2024-4-9测试通过"""
class Vertex:
    def __init__(self, num):
        self.num = num
        self.connected_to = {}

    def degree(self):
        return len(self.connected_to)

    def judge(self, num):
        return num in self.connected_to

    def add(self, num):
        self.connected_to[num] = True


class Graph:
    def __init__(self):
        self.vertexes = {}

    def add_vertex(self, num):
        vertex = Vertex(num)
        self.vertexes[num] = vertex

    def add_edge(self, a, b):
        self.vertexes[a].add(b)

    def judge(self, a, b):
        return self.vertexes[a].judge(b)


n, m = map(int, input().split())
graph = Graph()

for i in range(n):
    graph.add_vertex(i)

for _ in range(m):
    a, b = map(int, input().split())
    graph.add_edge(a, b)
    graph.add_edge(b, a)

l = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        l[i][j] = -graph.judge(i, j)
        if i == j:
            l[i][j] += graph.vertexes[i].degree()
for s in l:
    print(' '.join(map(str, s)))