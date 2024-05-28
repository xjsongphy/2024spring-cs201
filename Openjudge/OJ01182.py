"""于2024-5-23测试通过"""
class Circle:
    def __init__(self, root):
        self.kinds = {root: 0}
        self.root = root

    def join(self, circle, rotate):
        for idx, kind in circle.kinds.items():
            self.kinds[idx] = (kind - rotate) % 3
            ls[idx] = self.root


n, k = map(int, input().split())
ls = [i for i in range(n)]
circles = [Circle(i) for i in range(n)]
ans = 0

for _ in range(k):
    d, x, y = map(int, input().split())
    if x > n or y > n or (d == 2 and x == y):
        ans += 1
        continue
    x -= 1
    y -= 1

    idx_x = circles[ls[x]].kinds[x]
    idx_y = circles[ls[y]].kinds[y]
    if d == 1:
        if ls[x] != ls[y]:
            circles[ls[x]].join(circles[ls[y]], (idx_y - idx_x) % 3)
        else:
            if idx_x != idx_y:
                ans += 1
        continue

    if ls[x] != ls[y]:
        circles[ls[x]].join(circles[ls[y]], (idx_y - idx_x - 1) % 3)
    elif (idx_y - idx_x - 1) % 3 != 0:
        ans += 1

print(ans)