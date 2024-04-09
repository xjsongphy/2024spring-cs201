"""于2024-4-3测试通过"""
from heapq import *

n = int(input())
heap = list(map(int, input().split()))
heapify(heap)
w = 0

for _ in range(n - 1):
    a = heappop(heap)
    b = heappop(heap)
    w += a + b
    heappush(heap, a + b)
print(w)