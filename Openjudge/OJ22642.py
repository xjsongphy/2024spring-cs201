"""于2024-3-16测试通过"""
n = int(input())
ans = []


def dfs(single, left_out, right, step):
    if right == 0:
        global ans
        ans += step
        return

    if left_out > 0:
        dfs(single + 1, left_out - 1, right, [i + '(' for i in step])
    if single > 0:
        dfs(single - 1, left_out, right - 1, [i + ')' for i in step])


dfs(0, n, n, [''])
for i in ans:
    print(i)