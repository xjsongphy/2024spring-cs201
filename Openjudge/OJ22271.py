"""于2024-5-22测试通过"""
n = int(input())
trees = {}
for _ in range(n):
    s = input()
    if s not in trees:
        trees[s] = 0
    trees[s] += 1

for tree, num in sorted((tree, num) for tree, num in  trees.items()):
    print(f'{tree} {100 * num / n:.4f}%')