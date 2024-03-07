"""于2024-3-6测试通过"""
ans = []
n = 0

while True:
    try:
        s = input().split()
    except EOFError:
        break
    if s[0] == 'min':
        if n > 0:
            print(ans[-1])
    elif s[0] == 'pop':
        if n > 0:
            ans.pop()
            n -= 1
    else:
        weight = int(s[1])
        if n > 0:
            ans.append(min(ans[-1], weight))
        else:
            ans.append(weight)
        n += 1
