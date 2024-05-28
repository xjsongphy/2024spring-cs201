"""于2024-5-22测试通过"""
n = int(input())
edges = {}
for i in range(1, n + 1):
    l, r = map(int, input().split())
    edges[i] = (l, r)
father = [True]*n
for l, r in edges.values():
    if l != -1:
        father[l - 1] = False
    if r != -1:
        father[r - 1] = False
root = 0
for i in range(1, n + 1):
    if father[i - 1]:
        root = i
        break

def union(a, b):
    ans = []
    if len(b) <= len(a):
        for i in range(len(b)):
            ans.append(a[i] + b[i])
        ans += a[len(b):]
    else:
        for i in range(len(a)):
            ans.append(a[i] + b[i])
        ans += b[len(a):]

    return ans


def level(i):
    if i == -1:
        return []

    l = level(edges[i][0])
    r = level(edges[i][1])

    return [[i]] + union(l, r)


ans = level(root)
for i in range(len(ans)):
    ans[i] = str(ans[i][-1])
print(' '.join(ans))
