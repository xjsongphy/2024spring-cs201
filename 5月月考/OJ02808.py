l, m = map(int, input().split())
ls = [1]*(l + 1)
for _ in range(m):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        ls[i] = 0
print(sum(ls))