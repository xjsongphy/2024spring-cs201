"""于2024-3-6测试通过"""
s = input()
n = len(s)
s = int('0b' + s, 2)
ans = []

for _ in range(n):
    ans.append('0' if s % 5 else '1')
    s >>= 1
ans.reverse()
print(''.join(ans))