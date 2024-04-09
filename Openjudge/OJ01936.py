"""于2024-4-3测试通过"""
while True:
    try:
        s, t = input().split()
    except EOFError:
        break
    idx = 0
    ls, lt = len(s), len(t)
    found = False
    for c in s:
        found = False
        while True:
            if idx >= lt:
                break
            elif t[idx] == c:
                found = True
                idx += 1
                break
            idx += 1
        if not found:
            break
    if found:
        print('Yes')
    else:
        print('No')