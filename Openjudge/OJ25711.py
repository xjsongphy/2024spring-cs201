"""于2024-4-3测试通过"""
n, m = map(int, input().split())


def gpa(score):
    return 0 if score < 60 else (4 - 3*(100 - score)**2/1600)


ls = []
for _ in range(n):
    t = list(map(int, input().split()))
    id = t[0]
    ave = sum([gpa(t[2 * i + 1]) * t[2 * i + 2] for i in range(len(t) // 2)]) / sum(t[2::2])
    ls.append((ave, id))
ls.sort(reverse=True)
print(' '.join([str(tp[1]) for tp in ls[:m]]))

