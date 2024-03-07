"""于2024-3-5测试通过"""
dic = {'+': 1, '-': 2, '*': 3, '/': 4}
for _ in range(int(input())):
    ls = input().split()
    n = len(ls)
    stack = [float(ls[0])]
    idx = 1
    while idx < n:
        if ls[idx] in dic:
            a2 = stack.pop()
            a1 = stack.pop()
            t = dic[ls[idx]]
            if t < 4:
                stack.append([a1 + a2, a1 - a2, a1 * a2][t - 1])
            else:
                stack.append(a1 / a2)
        else:
            stack.append(float(ls[idx]))
        idx += 1
    print('%.2f' % stack[0])

