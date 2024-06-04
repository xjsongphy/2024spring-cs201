"""于2024-5-29测试通过"""
letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
idxes = {letters[i]: i for i in range(26)}
while True:
    n, m = map(int, input().split())
    if n == 0:
        break

    edges = {i: {} for i in range(n)}
    words = letters[:n]
    occurred = [0]*n
    pr = True
    for count in range(m):
        a, b = input().split('<')

        if not pr:
            continue
        elif a == b:
            pr = False
            print(f'Inconsistency found after {count + 1} relations.')
            continue

        a, b = idxes[a], idxes[b]
        edges[a][b] = True
        occurred[a] = occurred[b] = 1

        def check():
            in_degree = {i: 0 for i in range(n)}
            stack = []
            ans = []
            available = True

            for i in range(n):
                for j in edges[i]:
                    in_degree[j] += 1
            for i in range(n):
                if in_degree[i] == 0 and occurred[i]:
                    stack.append(i)

            while stack:
                if len(stack) > 1:
                    available = False

                idx = stack.pop()
                ans.append(letters[idx])
                for i in edges[idx]:
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        stack.append(i)

            return ans, available

        t, available = check()
        if len(t) == sum(occurred) == n and pr and available:
            print(f'Sorted sequence determined after {count + 1} relations: {"".join(t)}.')
            pr = False
        elif len(t) != sum(occurred) and pr:
            print(f'Inconsistency found after {count + 1} relations.')
            pr = False
    if pr:
        print('Sorted sequence cannot be determined.')