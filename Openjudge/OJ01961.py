"""于2024-6-4测试通过"""
case = 0
while True:
    n = int(input())
    if n == 0:
        break

    case += 1
    print(f"Test case #{case}")
    s = input()
    ne = [0]*n
    for i in range(1, n):
        if ne[i - 1] == 0:
            ne[i] = (s[i] == s[0])
        else:
            idx = ne[i - 1]
            while True:
                if idx == 0 and s[0] != s[i]:
                    ne[i] = 0
                    break

                if s[i] == s[idx]:
                    ne[i] = idx + 1
                    break
                else:
                    idx = ne[idx - 1]

        if (i + 1) % (i + 1 - ne[i]) == 0 and ne[i]:
            print(i + 1, (i + 1) // (i + 1 - ne[i]))
    print()

# case = 0
# while True:
#     n = int(input())
#     if n == 0:
#         break
#
#     case += 1
#     print(f"Test case #{case}")
#     s = input()
#     ans = {}
#     for i in range(1, n):
#         k = 1
#         while (k + 1)*i <= n and s[:i] == s[k*i:(k+1)*i]:
#             k += 1
#             if i*k not in ans:
#                 ans[i*k] = k
#     for r in ans.items():
#         print(*r)
#     print()