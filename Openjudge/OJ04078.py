"""于2024-3-26测试通过"""
def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


class BinHeap:
    def __init__(self):
        self.ls = []
        self.size = 0

    def insert(self, x):
        self.ls.append(x)
        self.size += 1

        idx = self.size - 1
        while True:
            if idx == 0:
                break

            p = parent(idx)
            if self.ls[p] > self.ls[idx]:
                self.ls[p], self.ls[idx] = self.ls[idx], self.ls[p]
            else:
                break

            idx = p

    def pop(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            self.size -= 1
            return self.ls.pop()

        s = self.ls[0]
        self.ls[0] = self.ls[-1]
        self.ls.pop()
        self.size -= 1

        idx = 0
        while True:
            l, r = left(idx), right(idx)

            if l < self.size and r < self.size:
                if self.ls[l] < self.ls[r]:
                    if self.ls[idx] > self.ls[l]:
                        self.ls[idx], self.ls[l] = self.ls[l], self.ls[idx]
                        idx = l
                    else:
                        break
                else:
                    if self.ls[idx] > self.ls[r]:
                        self.ls[idx], self.ls[r] = self.ls[r], self.ls[idx]
                        idx = r
                    else:
                        break
            elif l < self.size and self.ls[idx] > self.ls[l]:
                self.ls[idx], self.ls[l] = self.ls[l], self.ls[idx]
                idx = l
            elif r < self.size and self.ls[idx] > self.ls[r]:
                self.ls[idx], self.ls[r] = self.ls[r], self.ls[idx]
                idx = r
            else:
                break
        return s


ans = []
heap = BinHeap()
for _ in range(int(input())):
    ls = input().split()
    if ls[0] == '2':
        ans.append(str(heap.pop()))
    else:
        heap.insert(int(ls[1]))
print('\n'.join(ans))