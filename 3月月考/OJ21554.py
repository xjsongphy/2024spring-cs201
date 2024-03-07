"""于2024-3-6测试通过"""
n = int(input())
ls = list(map(int, input().split()))
ls = sorted([(ls[i], i + 1) for i in range(n)])
time = 0
total_time = 0
for i in range(n):
    total_time += time
    time += ls[i][0]
print(' '.join([str(s[1]) for s in ls]))
print('%.2f' % (total_time / n))
