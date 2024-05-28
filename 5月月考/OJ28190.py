n = int(input())
ls = [int(input()) for _ in range(n)]
i = 0
ans = 0
next_i = 1
while i < n - 1:
    if ls[i] >= ls[i + 1]:
        i += 1
        next_i = i + 1
        continue
    mid_max = ls[i + 1]
    ans = max(ans, 2)
    j = i + 2
    while j < n:
        if ls[j] > mid_max:
            ans = max(ans, j - i + 1)
            mid_max = ls[j]
            j += 1
            next_i = j
        else:
            if ls[j] <= ls[i]:
                break
            else:
                j += 1
    i = next_i
    next_i += 1
print(ans)