"""于2024-6-4测试通过"""
stack = []
n = int(input())
h = [int(input()) for _ in range(n)]
left, right = [0]*n, [0]*n

for i in range(n):
    while stack and h[stack[-1]] >= h[i]:
        right[stack.pop()] = i
    stack.append(i)
while stack:
    right[stack.pop()] = n

for i in range(n - 1, -1, -1):
    while stack and h[stack[-1]] <= h[i]:
        left[stack.pop()] = i
    stack.append(i)
while stack:
    left[stack.pop()] = -1

ans = 0
for i in range(n):
    if i - left[i] <= ans:
        continue
    for j in range(left[i] + 1, i):
        if right[j] > i:
            ans = max(ans, i - j + 1)
print(ans)

