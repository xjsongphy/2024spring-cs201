for _ in range(int(input())):
    n, m = map(int, input().split())
    edges = [[-1, -1, -1] for __ in range(n)]
    root = [1] * n
    for __ in range(n):
        x, y, z = map(int, input().split())
        edges[x][1], edges[x][2] = y, z
        edges[y][0] = edges[z][0] = x
        root[y] = root[z] = 0

    root = root.index(1)
    for __ in range(m):
        s = input().split()
        if s[0] == '1':
            t, x, y = map(int, s)
            father_x, father_y = edges[x][0], edges[y][0]
            idx_x, idx_y = edges[father_x].index(x), edges[father_y].index(y)

            edges[father_x][idx_x], edges[father_y][idx_y] = y, x
            edges[x][0], edges[y][0] = father_y, father_x
        else:
            x = int(s[1])
            while edges[x][1] != -1:
                x = edges[x][1]
            print(x)
