"""于2024-3-12测试通过"""
x = list(input())
x.reverse()
n = len(x)

while True:
    try:
        s = input()
    except EOFError:
        break

    if sorted(x) != sorted(s):
        print('NO')
        continue

    ls = x[:]
    stack = []

    matched = False

    for i in range(n):
        matched = False
        if stack:
            if stack[-1] == s[i]:
                stack.pop()
                matched = True
        if matched:
            continue
        while ls:
            if ls[-1] == s[i]:
                ls.pop()
                matched = True
                break
            else:
                stack.append(ls.pop())
        if not matched:
            print('NO')
            break

    if matched:
        print('YES')