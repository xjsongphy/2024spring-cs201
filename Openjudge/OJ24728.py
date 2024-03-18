"""于2024-3-16测试通过"""


def split_tree(tree):
    if not tree:
        return []

    ans = []
    cnt = 0
    start = 0
    for i, c in enumerate(tree):
        if c == '(':
            cnt += 1
        elif c == ')':
            cnt -= 1
        if c == ',' and cnt == 0:
            ans.append(tree[start: i])
            start = i + 1

    ans.append(tree[start:])
    return ans


def front(tree):
    if not tree:
        return ''

    ans = tree[0]
    for child in split_tree(tree[2: -1]):
        ans += front(child)

    return ans


def back(tree):
    if not tree:
        return ''

    ans = ''
    for child in split_tree(tree[2: -1]):
        ans += back(child)

    return ans + tree[0]


tree = input()
print(front(tree))
print(back(tree))
