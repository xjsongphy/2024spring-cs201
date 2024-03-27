"""于2024-3-27测试通过"""
ans = ''
while True:
    try:
        n = int(input())
    except EOFError:
        break
    ls = [int(input()) for _ in range(n)]
    ls.reverse()


    def merge_sort(i, j):
        if j <= i:
            return 0
        mid = (i + j) >> 1
        t = merge_sort(i, mid) + merge_sort(mid + 1, j)

        temp = ls[i: j + 1]
        mid -= i
        l, r = 0, mid + 1
        for idx in range(i, j + 1):
            if l > mid:
                ls[idx] = temp[r]
                r += 1
            elif r > j - i:
                ls[idx] = temp[l]
                l += 1
            elif temp[l] <= temp[r]:
                ls[idx] = temp[l]
                l += 1
            else:
                ls[idx] = temp[r]
                r += 1
                t += mid - l + 1

        return t
    ans += str(merge_sort(0, n - 1)) + '\n'
    input()
print(ans)