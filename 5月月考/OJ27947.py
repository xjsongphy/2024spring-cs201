from heapq import *
for _ in range(int(input())):
    ls = list(map(int, input().split()))
    ls.reverse()
    n = len(ls)
    left_heap, right_heap = [], []
    mid = ls.pop()
    ans = [str(mid)]
    while ls:
        a = ls.pop()
        if not ls:
            break
        b = ls.pop()
        l, r = 0, 0
        if a >= mid:
            heappush(right_heap, a)
            r += 1
        else:
            heappush(left_heap, -a)
            l += 1
        if b >= mid:
            heappush(right_heap, b)
            r += 1
        else:
            heappush(left_heap, -b)
            l += 1
        while r > l:
            t = heappop(right_heap)
            heappush(left_heap, -mid)
            mid = t
            r -= 1
            l += 1
        while l > r:
            t = -heappop(left_heap)
            heappush(right_heap, mid)
            mid = t
            r += 1
            l -= 1
        ans.append(str(mid))
    print(len(ans))
    print(' '.join(ans))