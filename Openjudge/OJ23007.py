"""于2024-4-3测试通过"""
from functools import cmp_to_key

def key(s1, s2):
    if s1 == s2:
        return 0

    s1 = list(map(int, s1.split('.')))
    s2 = list(map(int, s2.split('.')))

    l = min(len(s1), len(s2))
    for i in range(l):
        if s1[i] < s2[i]:
            return -1
        elif s1[i] > s2[i]:
            return 1

    return len(s1) - len(s2)


ls = [input() for _ in range(int(input()))]
ls.sort(key=cmp_to_key(key))
print('\n'.join(ls))