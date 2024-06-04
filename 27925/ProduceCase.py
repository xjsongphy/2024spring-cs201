def generate_input(case, seed):
    import random

    random.seed(seed)

    n = random.randint(1, 50)
    # n = 2
    t = []
    for _ in range(n):
        t.append(random.randint(3, 500))
        # t.append(random.randint(3, 6))
    all_num = list(range(1000000))
    # all_num = list(range(100))

    all_sample = random.sample(all_num, sum(t))

    ids = []
    cur = 0
    for i in range(n):
        ids.append(all_sample[cur : cur + t[i]])
        cur += t[i]

    from queue import Queue

    team_ids = dict()

    for i in range(n):
        for x in ids[i]:
            team_ids[x] = i

    team = Queue()
    person = [Queue() for _ in range(n)]
    not_in = set(all_sample)  # not in queue

    out_path = f"./data/{case}.in"
    with open(out_path, "w") as f:
        f.write(f"{n}\n")
        for i in range(n):
            f.write(f"{' '.join(map(str, ids[i]))}\n")

        i = 0
        while True:
            choices = []
            # if i > 6:
            #     choices.append("STOP")
            if not team.empty():
                # print("team", team.queue)
                choices.append("DEQUEUE")
            if i < len(all_sample):
                # print("all_sample", len(all_sample))
                choices.append(f"ENQUEUE")

            op = None
            if choices == []:
                op = "STOP"
            else:
                op = random.choice(choices)

            if op == "STOP":
                f.write("STOP\n")
                break

            elif op == "ENQUEUE":
                # draw a number from not_in
                x = all_sample[i]
                # delete it from not_in
                not_in.remove(x)
                if person[team_ids[x]].empty():
                    team.put(team_ids[x])
                person[team_ids[x]].put(x)
                f.write(f"ENQUEUE {x}\n")
                i += 1

            elif op == "DEQUEUE":
                id_ = team.queue[0]
                f.write(f"DEQUEUE\n")
                person[id_].get()
                if person[id_].empty():
                    team.get()
            else:
                raise ValueError(f"Unknown operation {op}")

            # print(i, op, team.queue, [p.queue for p in person], not_in)


def generate_output(case):
    import os

    in_path = f"./data/{case}.in"
    out_path = f"./data/{case}.out"
    os.system(f"python SampleCode.py < {in_path} > {out_path}")


def main():
    import os

    os.makedirs("data/", exist_ok=True)

    n_case = 20
    for i in range(n_case):
        # random seed
        seed = 100 + i
        generate_input(i, seed)
        generate_output(i)


if __name__ == "__main__":
    main()
