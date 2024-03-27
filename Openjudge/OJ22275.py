"""于2024-3-26测试通过"""
n = int(input())
front = list(map(int, input().split()))


def front_to_back(front):
    if not front:
        return []

    first = front[0]
    left_front, right_front = [], []
    for i in range(1, len(front)):
        if front[i] < first:
            left_front.append(front[i])
        else:
            right_front = front[i:]
            break

    return front_to_back(left_front) + front_to_back(right_front) + [first]


print(' '.join(map(str, front_to_back(front))))
