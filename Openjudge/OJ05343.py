"""于2024-6-4测试通过"""
n = int(input())
ls = input().split()
queues_x = [[] for _ in range(4)]
queues_y = [[] for _ in range(9)]
indexes = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
for t in ls:
    queues_y[int(t[1]) - 1].append(t)
queue = []
for i in range(1, 10):
    print(f'Queue{i}:{" ".join(queues_y[i - 1])}')
    queue += queues_y[i - 1]
for t in queue:
    queues_x[indexes[t[0]]].append(t)
queue = []
for i in indexes:
    print(f'Queue{i}:{" ".join(queues_x[indexes[i]])}')
    queue += queues_x[indexes[i]]
print(*queue)