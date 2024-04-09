"""于2024-4-3测试通过"""
n, m = map(int, input().split())
dp = [0] * (m + 1)
for _ in range(n):
    need, value = map(int, input().split())
    if need > m:
        continue
    for i in range(m, need - 1, -1):
        dp[i] = max(dp[i], dp[i - need] + value)
print(dp[-1])