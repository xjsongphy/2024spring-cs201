"""于2024-3-18测试通过"""


def mid_back_to_front(mid, back):
    if not mid:
        return ''

    idx = mid.index(back[-1])
    left_mid = mid[:idx]
    right_mid = mid[idx + 1:]
    left_back = back[:idx]
    right_back = back[idx:-1]

    return back[-1] + mid_back_to_front(left_mid, left_back) + mid_back_to_front(right_mid, right_back)


mid = input()
back = input()
print(mid_back_to_front(mid, back))