"""于2024-3-6测试通过"""
n = int(input())
ls = list(map(int, input().split()))
dp = [0] * n
dp[-1] = 1

for i in range(n - 2, -1, -1):
    for j in range(i, n):
        if ls[i] >= ls[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))