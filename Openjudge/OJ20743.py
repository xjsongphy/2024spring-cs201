"""于2024-3-19测试通过"""
s = input()


def rev(s):
    idx = cnt = 0
    ans = ''
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
            if cnt == 1:
                idx = i
        elif s[i] == ')':
            cnt -= 1
            if cnt == 0:
                ans += rev(s[idx + 1: i])[:: -1]
        elif cnt == 0:
            ans += s[i]

    return ans


print(rev(s))