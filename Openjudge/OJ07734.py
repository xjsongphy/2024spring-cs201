"""于2024-5-28测试通过"""
import sys
input = lambda: sys.stdin.readline().strip()
write = lambda x: sys.stdout.write(str(x))

circles = []
roots = []
ans = ''


class Circle:
    def __init__(self, root):
        self.sexes = {root: True}
        self.root = root

    def join(self, circle, rotate):
        if rotate:
            for idx, sex in circle.sexes.items():
                self.sexes[idx] = not sex
                roots[idx] = self.root
            return

        for idx, sex in circle.sexes.items():
            self.sexes[idx] = sex
            roots[idx] = self.root


for i in range(int(input())):
    n, m = map(int, input().split())
    circles = [None for j in range(n)]
    roots = list(range(n))

    suspicious = False
    for _ in range(m):
        a, b = map(int, input().split())
        if a == b:
            suspicious = True
            continue

        a -= 1
        b -= 1
        if not circles[a] and roots[a] == a:
            if not circles[b] and roots[b] == b:
                circles[a] = Circle(a)
                circles[a].sexes[b] = False
                roots[b] = a
            else:
                circles[roots[b]].sexes[a] = not circles[roots[b]].sexes[b]
                roots[a] = roots[b]
            continue
        elif not circles[b] and roots[b] == b:
            circles[roots[a]].sexes[b] = not circles[roots[a]].sexes[a]
            roots[b] = roots[a]
        if roots[a] == roots[b] and circles[roots[a]].sexes[a] == circles[roots[b]].sexes[b]:
            suspicious = True
        elif roots[a] != roots[b]:
            circles[roots[a]].join(circles[roots[b]], circles[roots[a]].sexes[a] == circles[roots[b]].sexes[b])
    ans += f'Scenario #{i + 1}:\n' + ['No suspicious bugs found!\n\n', 'Suspicious bugs found!\n\n'][suspicious]
write(ans)