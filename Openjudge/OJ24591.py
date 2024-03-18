""""""
for _ in range(int(input())):
    s = input().strip()
    ans = []
    op = []
    operators = {'+': 1, '-': 1, '*': 2, '/': 2}
    dic = {i: True for i in '0123456789.'}

    idx = 0
    n = len(s)
    while idx < n:
        if s[idx] in dic:
            i = idx
            while i < n and s[i] in dic:
                i += 1
            ans.append(s[idx: i])
            idx = i - 1
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
        print(f'{" ".join(ans)} {" ".join(op)}')
    else:
        print(" ".join(ans))