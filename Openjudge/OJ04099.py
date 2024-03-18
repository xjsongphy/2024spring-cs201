"""于2024-3-16测试通过"""
for _ in range(int(input())):
    err = False
    q = []
    stack = []

    for __ in range(int(input())):
        s = input().split()
        if s[0] == 'pop':
            if stack:
                q.pop(0)
                stack.pop()
            else:
                err = True
        else:
            q.append(s[1])
            stack.append(s[1])

    if err:
        print('error\nerror')
    else:
        print(' '.join(q))
        print(' '.join(stack))