import random
import time

random.seed(1)

for epoch in range(20):
    n = random.randint(2, 10**6)
    print(n)

    values = [random.randint(2**30, 2**31-1) for _ in range(n)]

    inlines = [f'{n}\n'] + ['\n'.join(map(str, values)) + '\n']

    with open(f'data/{epoch}.in', 'w') as f:
        f.writelines(inlines)

    start = time.time()

    #N = int(input())
    #heights = [int(input()) for _ in range(N)]
    N = n
    heights = values

    left_bound = [-1] * N
    right_bound = [N] * N

    stack = []

    for i in range(N):
        while stack and heights[stack[-1]] < heights[i]:
            stack.pop()

        if stack:
            left_bound[i] = stack[-1]

        stack.append(i)

    stack = []

    for i in range(N - 1, -1, -1):
        while stack and heights[stack[-1]] > heights[i]:
            stack.pop()

        if stack:
            right_bound[i] = stack[-1]

        stack.append(i)

    ans = 0

    for i in range(N - 1, -1, -1):
        for j in range(left_bound[i] + 1, i):
            if right_bound[j] > i:
                ans = max(ans, i - j + 1)
                break

        if i <= ans:
            break

    print(ans)

    end = time.time() - start

    print(f"[{epoch}] {end:.3f}sec")
    #print(ans)

    # res = ' '.join(map(str, res))
    res = ans
    with open(f'data/{epoch}.out', 'w') as f:
        f.writelines([str(res) + '\n'])


