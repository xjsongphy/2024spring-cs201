"""于2024-6-3测试通过"""
from heapq import *

n = int(input())
heap = [int(input()) for _ in range(n)]
heapify(heap)
cost = 0

while len(heap) > 1:
    a, b = heappop(heap), heappop(heap)
    cost += a + b
    heappush(heap, a + b)
print(cost)