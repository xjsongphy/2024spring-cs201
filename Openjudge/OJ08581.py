"""于2024-4-20测试通过"""
front = input()
idx = 0


def mid():
    global idx
    if front[idx] == '.':
        idx += 1
        return ''

    root = front[idx]
    idx += 1

    return mid() + root + mid()


def back():
    global idx
    if front[idx] == '.':
        idx += 1
        return ''

    root = front[idx]
    idx += 1

    return back() + back() + root


print(mid())
idx = 0
print(back())