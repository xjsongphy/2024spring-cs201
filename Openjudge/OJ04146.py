"""于2024-3-19测试通过"""
n = int(input())
ans = 0

for a1 in range(n + 1):
    a2 = [0, 1][a1 % 2]
    while a2 <= n:
        a3 = n - (a2 + n) % 3
        while True:
            if a3 >= 0 and (a1 + a2 + a3) % 5 == 0:
                ans = max(ans, a1 + a2 + a3)
                break
            a3 -= 3
            if a3 < 0:
                break
        a2 += 2

print(ans)