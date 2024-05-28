from queue import Queue

while True:
    try:
        n = int(input())
    except EOFError:
        break
    edges = {i: {} for i in range(n)}
    t = []
    for i in range(n):
        ls = list(map(int, input().split()))
        for j in range(i + 1, n):
            t.append((ls[j], i, j))
    t.sort()
    ans = 0
    for idx in range(len(t)):
        cost, a, b = t[idx]
        edges[a][b] = edges[b][a] = True
        not_visited = [True] * n
        visited_edges = {}
        loop = False
        q = Queue()
        q.put(a)
        while not q.empty():
            i = q.get()
            if not not_visited[i]:
                loop = True
                break
            not_visited[i] = False
            for j in edges[i]:
                if (i, j) in visited_edges:
                    continue
                visited_edges[(i, j)] = True
                visited_edges[(j, i)] = True
                q.put(j)
        if loop:
            del edges[a][b]
            del edges[b][a]
        else:
            ans += cost
    print(ans)