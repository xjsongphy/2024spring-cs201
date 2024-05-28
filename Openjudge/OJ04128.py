"""于2024-5-28测试通过"""
from queue import Queue

start, end = input().split()
words = input().split()
words.append(end)
edges = {}
visited = {}

for i in range(len(words)):
    word = words[i]
    for j in range(len(word)):
        key = word[:j] + '_' + word[j + 1:]
        if key not in edges:
            edges[key] = {}
        edges[key][i] = True

q = Queue()
q.put((start, 1))
while not q.empty():
    word, l = q.get()
    if word == end:
        print(l)
        exit()
    if word in visited:
        continue
    visited[word] = True
    l += 1

    possibles = {}
    for i in range(len(word)):
        key = word[:i] + '_' + word[i + 1:]
        if key not in edges:
            continue
        for j in edges[key]:
            if words[j] in visited:
                continue
            possibles[words[j]] = None

    for possible in possibles:
        q.put((possible, l))
print(0)
