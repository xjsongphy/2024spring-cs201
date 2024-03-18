"""于2024-3-16测试通过"""
while True:
    try:
        s = input()
    except EOFError:
        break

    raw = int(s)
    s = list(s)
    s.reverse()
    s = ''.join(s)
    s.lstrip('0')
    rev = int(s)
    print('YES' if raw == rev else 'NO')