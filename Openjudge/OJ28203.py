""""""
n = int(input())
ls = list(map(int, input().split()))
stack = []
for i in range(1, n + 1):
    while stack:
        if ls[stack[-1] - 1] < ls[i - 1]:
            ls[stack.pop() - 1] = str(i)
        else:
            stack.append(i)
            break
    if not stack:
        stack.append(i)
while stack:
    ls[stack.pop() - 1] = '0'
print(' '.join(ls))