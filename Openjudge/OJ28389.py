"""于2024-6-2测试通过"""
from bisect import *

n = int(input())
ls = list(map(int, input().split()))
heights = []
for t in ls:
    if not heights:
        heights.append(t)
        continue

    idx = bisect_right(heights, t) - 1
    if idx < 0:
        heights = [t] + heights
    else:
        heights[idx] = t
print(len(heights))