while True:
    s = input()
    if s == '.':
        break

    l = len(s)
    for i in range(1, l + 1):
        if l % i != 0:
            continue
        n = l // i
        if s[:i]*n == s:
            print(n)
            break