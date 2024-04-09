"""于2024-4-9测试通过"""
class Node:
    def __init__(self):
        self.child = {}


class TrieTree:
    def __init__(self):
        self.root = Node()

    def add(self, s):
        p = self.root
        for _ in range(len(s) - 1):
            t = s.pop()
            if t not in p.child:
                p.child[t] = Node()
            p = p.child[t]

    def judge(self, s):
        p = self.root
        ans = True
        for _ in range(len(s)):
            t = s.pop()
            if t in p.child:
                p = p.child[t]
            else:
                ans = False
                break

        return ans


for _ in range(int(input())):
    trie = TrieTree()
    nums = {}
    ans = True
    for _ in range(int(input())):
        s = input()
        t = list(s)
        t.reverse()
        s = ''.join(t)
        if s in nums:
            ans = False

        nums[s] = True
        trie.add(t)

    for num in nums:
        if trie.judge(list(num)):
            ans = False
    print('YES' if ans else 'NO')


# for _ in range(int(input())):
#     pre = {}
#     nums = {}
#     ans = True
#     for _ in range(int(input())):
#         s = input()
#         if s in nums:
#             ans = False
#
#         nums[s] = True
#         for i in range(1, len(s)):
#             if i in pre:
#                 pre[i][s[:i]] = True
#             else:
#                 pre[i] = {s[:i]: True}
#
#     for num in nums:
#         l = len(num)
#         if l in pre:
#             if num in pre[l]:
#                 ans = False
#                 break
#
#     print('YES' if ans else 'NO')