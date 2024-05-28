""""""
for _ in range(int(input())):
    n, m = map(int, input().split())
    edges = {i: [0, 0, 0] for i in range(n)}
    for i in range(n):
        x, y, z = map(int, input().split())
        edges[x][1], edges[x][2] = y, z
        if y != -1:
            edges[y][0] = x
        if z != -1:
            edges[z][0] = x
    for __ in range(m):
        s = list(map(int, input().split()))
        if s[0] == 1:
            x, y = s[1], s[2]
            x_father, y_father = edges[x][0], edges[y][0]
            x_idx, y_idx = 1 + (edges[x_father][2] == x), 1 + (edges[y_father][2] == y)
            edges[x_father][x_idx], edges[y_father][y_idx], edges[x][0], edges[y][0] = y, x, y_father, x_father
        else:
            x = s[1]
            while edges[x][1] != -1:
                x = edges[x][1]
            print(x)