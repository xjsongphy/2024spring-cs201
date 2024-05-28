from queue import Queue

n, m = map(int, input().split())
edges = {i: {} for i in range(n)}
for _ in range(m):
    a, b = map(int, input().split())
    edges[a][b] = edges[b][a] = True

not_visited = [True]*n
q = Queue()
q.put(0)
while not q.empty():
    i = q.get()
    if not not_visited[i]:
        continue
    not_visited[i] = False
    for j in edges[i]:
        if not_visited[j]:
            q.put(j)
print(f'connected:{["yes", "no"][sum(not_visited) > 0]}')

not_visited = [True]*n
visited_edges = {}
loop = False
for i in range(n):
    if not not_visited[i]:
        continue
    q = Queue()
    q.put(i)
    while not q.empty():
        j = q.get()
        if not not_visited[j]:
            loop = True
            break
        not_visited[j] = False
        for k in edges[j]:
            if (k, j) in visited_edges:
                continue
            visited_edges[(k, j)] = True
            visited_edges[(j, k)] = True
            q.put(k)
    if loop:
        break
print(f'loop:{["no", "yes"][loop]}')