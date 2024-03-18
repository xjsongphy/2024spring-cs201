""""""


def front_mid_to_back(front, mid):
    if not mid:
        return ''

    idx = mid.index(front[0])
    left_front = front[1: idx + 1]
    right_front = front[idx + 1:]
    left_mid = mid[: idx]
    right_mid = mid[idx + 1:]

    return front_mid_to_back(left_front, left_mid) + front_mid_to_back(right_front, right_mid) + front[0]


while True:
    try:
        front = input()
        mid = input()
    except EOFError:
        break
    print(front_mid_to_back(front, mid))