count = 1
while True:
    p, e, i, d = map(int, input().split())
    if d + p + e + i == -4:
        break
    p, e, i = p - d, e - d, i - d
    ls = [0, 0]
    dist = 33
    day = i % 33
    while True:
        if (day - p) % 23 == ls[0] == 0:
            dist *= 23
            ls[0] = 1
        if (day - e) % 28 == ls[1] == 0:
            dist *= 28
            ls[1] = 1
        if ls[0] == ls[1] == 1 and day > 0:
            print(f'Case {count}: the next triple peak occurs in {day} days.')
            break
        day += dist
    count += 1