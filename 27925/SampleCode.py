from queue import Queue

team_id = dict()


def main():
    t = int(input())
    for i in range(t):
        members = list(map(int, input().split()))
        for x in members:
            team_id[x] = i

    team = Queue()
    person = [Queue() for _ in range(t)]

    i = 0
    while True:
        op = input()
        if op == "STOP":
            break
        if op.startswith("ENQUEUE"):
            x = int(op.split()[1])
            id_ = team_id[x]
            if person[id_].empty():
                team.put(id_)  # 如果没有这个人，把这个人的编号存入team队列中
            person[id_].put(x)  # 把这个人压入队列中
        else:
            # peek the first item
            id_ = team.queue[0]
            print(person[id_].get())
            if person[id_].empty():
                team.get()


if __name__ == "__main__":
    main()
