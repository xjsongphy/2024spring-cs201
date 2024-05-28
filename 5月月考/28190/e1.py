from bisect import bisect_right

h = []
low, high = [], []
i = -1
ans = 0
for o in range(int(input())):
    i += 1
    h.append(int(input()))
    while low and h[-1] <= h[low[-1]]:
        low.pop()
    low.append(i)
    while high and h[-1] >= h[high[-1]]:
        high.pop()
    high.append(i)
    ans = max(ans, i - low[bisect_right(low, high[-2] if len(high)>1 else -1)])
print(ans+1 if ans else 0)
