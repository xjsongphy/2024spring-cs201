"""于2024-3-12测试通过"""
n = int(input())

father = {i: None for i in range(1, n + 1)}
son = {i: [-1, -1] for i in range(1, n + 1)}

for i in range(1, n + 1):
    l, r = map(int, input().split())
    son[i] = [l, r]
    father[l] = father[r] = i


def h(idx):
    ans = 1

    l, r = son[idx]
    if l != -1:
        ans = max(ans, 1 + h(l))
    if r != -1:
        ans = max(ans, 1 + h(r))

    return ans


for key, value in father.items():
    if not value:
        print(h(key))
        break
