"""于2024-3-19测试通过"""


def mid_back_to_front(mid, back):
    if not mid:
        return ''

    idx = mid.index(back[-1])
    left_mid = mid[:idx]
    right_mid = mid[idx + 1:]
    left_back = back[:idx]
    right_back = back[idx:-1]

    left = mid_back_to_front(left_mid, left_back)
    right = mid_back_to_front(right_mid, right_back)

    ans = [left[i] + right[i] for i in range(min(len(left), len(right)))]
    ans += left[len(right):]
    ans += right[len(left):]

    return [back[-1]] + ans


for _ in range(int(input())):
    print(''.join(mid_back_to_front(input(), input())))