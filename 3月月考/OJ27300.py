"""于2024-3-6测试通过"""
n = int(input())
models = {}
for _ in range(n):
    s = input().split('-')
    if s[0] in models:
        models[s[0]].append(s[1])
    else:
        models[s[0]] = [s[1]]
for model in sorted(list(models.keys())):
    print(f'{model}: {", ".join(sorted(models[model], key=lambda t: float(t[:-1])*[1, 1000][t[-1] == "B"]))}')