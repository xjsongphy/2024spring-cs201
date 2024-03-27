"""于2024-3-26测试通过"""
cnt = 1
while True:
    n, m = map(int, input().split())
    if n == 0:
        break

    path = {i: set() for i in range(1, n + 1)}
    for _ in range(m):
        i, j = map(int, input().split())
        path[i].add(j)
        path[j].add(i)

    tags = {i: None for i in range(1, n + 1)}

    def searching(idx, tag):
        tags[idx] = tag
        for i in path[idx]:
            if not tags[i]:
                searching(i, tag)

    tag = 0
    for i in range(1, n + 1):
        if not tags[i]:
            tag += 1
            searching(i, tag)
    print(f'Case {cnt}: {tag}')
    cnt += 1
