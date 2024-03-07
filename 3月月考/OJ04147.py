"""于2024-3-6测试通过"""
n, a, b, c = input().split()
n = int(n)


def move(n, a, b, c):
    if n == 0:
        return
    move(n - 1, a, c, b)
    print(f'{n}:{a}->{b}')
    move(n - 1, c, b, a)


move(n, a, c, b)