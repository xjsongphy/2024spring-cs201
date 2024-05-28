s = input()
t = ''
for c in s:
    t += c
    print(1 if int('0b' + t, 2)%5 == 0 else 0, end='')