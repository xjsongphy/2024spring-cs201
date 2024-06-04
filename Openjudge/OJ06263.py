"""于2024-6-3测试通过"""
while True:
    try:
        s = input().replace('!', 'V!')
    except EOFError:
        break

    ans = []
    op = []
    operators = {'|': 1, '&': 2, '!': 3}

    idx = 0
    n = len(s)
    while idx < n:
        if s[idx] == ' ':
            idx += 1
            continue

        if s[idx] == 'V' or s[idx] == 'F':
            ans.append(1 if s[idx] == 'V' else 0)
        elif s[idx] == '(':
            op.append('(')
        elif s[idx] == ')':
            while op[-1] != '(':
                ans.append(op.pop())
            op.pop()
        else:
            if not op:
                op.append(s[idx])
            elif op[-1] == '(' or operators[op[-1]] < operators[s[idx]]:
                op.append(s[idx])
            else:
                while op and op[-1] != '(' and operators[op[-1]] >= operators[s[idx]]:
                    ans.append(op.pop())
                op.append(s[idx])
        idx += 1
    if op:
        op.reverse()
        ans = ans + op

    stack = []
    for c in ans:
        if c in operators:
            if c == '|':
                b, a = stack.pop(), stack.pop()
                stack.append(a | b)
            elif c == '&':
                b, a = stack.pop(), stack.pop()
                stack.append(a and b)
            if c == '!':
                a, b = stack.pop(), stack.pop()
                stack.append(not a)
        else:
            stack.append(c)
    print('V' if stack[0] else 'F')