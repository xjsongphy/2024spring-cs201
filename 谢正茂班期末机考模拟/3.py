n, k = map(int, input().split())
ls = []
for i in range(n):
    a, b = map(int, input().split())
    ls.append((a, b, i + 1))

ls = sorted(ls, reverse=True)[:k]
ls.sort(key=lambda t: t[1], reverse=True)
print(ls[0][2])