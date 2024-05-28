"""超内存，暴力法可过"""
words = {}
idx = 0
letters = 'abcdefghijklmnopqrstuvwxyz'

while True:
    s = input()
    if s == '#':
        break
    words[s] = idx
    idx += 1


p = {}


def insert(t):
    if t in words:
        p[t] = words[t]


while True:
    s = input()
    if s == '#':
        break
    if s in words:
        print(f'{s} is correct')
        continue
    p = {}
    for i in range(len(s)):
        for l in letters:
            insert(s[:i] + l + s[i + 1:])
    for i in range(len(s)):
        insert(s[:i] + s[i + 1:])
    for i in range(len(s) - 1):
        for l in letters:
            insert(s[:i + 1] + l + s[i + 1:])
    for l in letters:
        insert(l + s)
        insert(s + l)

    p = [i[1] for i in sorted((idx, key) for key, idx in p.items())]
    print(f'{s}: {" ".join(p)}')












# words = {}
# possibles = {}
#
#
# def insert(t):
#     if t not in possibles:
#         possibles[t] = []
#     possibles[t].append(words[s])
#
#
# def generate(idx, s):
#     if len(s) > 1:
#         for i in range(len(s)):
#             insert(s[:i] + s[i + 1:])
#     for i in range(len(s)):
#         insert(s[:i] + '*' + s[i + 1:])
#     for i in range(len(s) - 1):
#         insert(s[:i + 1] + '*' + s[i + 1:])
#     insert('*' + s)
#     insert(s + '*')
#
#
# idx = 0
# while True:
#     s = input()
#     if s == '#':
#         break
#     words[s] = idx
#     generate(idx, s)
#     idx += 1
#
# keys = list(words.keys())
#
# while True:
#     s = input()
#     if s == '#':
#         break
#     if s in words:
#         print(f'{s} is correct')
#         continue
#     p = {}
#     if s in possibles:
#         for k in possibles[s]:
#             p[keys[k]] = k
#     for i in range(len(s)):
#         t = s[:i] + '*' + s[i + 1:]
#         if t in possibles:
#             for k in possibles[t]:
#                 p[keys[k]] = k
#     p = [i[1] for i in sorted((idx, key) for key, idx in p.items())]
#     print(f'{s}: {" ".join(p)}')
# print(possibles)