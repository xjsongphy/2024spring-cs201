"""于2024-3-16测试通过"""
n = int(input())
ans = []
while n > 0:
    ans.append(n % 8)
    n = n // 8
ans.reverse()
print(''.join([str(i) for i in ans]))