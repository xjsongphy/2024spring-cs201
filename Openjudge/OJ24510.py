"""于2024-4-3测试通过"""
n = int(input())
dic = {}
for i in range(n):
    url, start, end = input().split()
    start = list(map(int, start.split(':')))
    end = list(map(int, end.split(':')))
    t = (end[0] - start[0]) * 3600 + (end[1] - start[1]) * 60 + end[2] - start[2]

    if url in dic:
        dic[url] += t
    else:
        dic[url] = t

print(max([(value, key) for key, value in dic.items()])[1])