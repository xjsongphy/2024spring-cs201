# Assignment #7: April 月考

Updated 1557 GMT+8 Apr 3, 2024

2024 spring, Complied by Xinjie Song, Phy



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



**编程环境**


操作系统：Windows 11 22H2

Python编程环境：PyCharm 2023.2 (Community Edition)

C/C++编程环境：g++ (x86_64-win32-seh-rev0, Built by MinGW-W64 project) 8.1.0



## 1. 题目

### 27706: 逐词倒放

http://cs101.openjudge.cn/practice/27706/



思路：懒得写栈了，直接反转



代码

```python
ls = input().split()
ls.reverse()
print(' '.join(ls))
```



代码运行截图 

![image-20240403184306653](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202404031843472.png)



### 27951: 机器翻译

http://cs101.openjudge.cn/practice/27951/



思路：队列



代码

```python
from queue import Queue

m, n = map(int, input().split())
q = Queue()
l = ans = 0
dic = {}
for s in input().split():
    if s not in dic or not dic[s]:
        ans += 1
        dic[s] = True
        q.put(s)
        l += 1
    if l > m:
        t = q.get()
        dic[t] = False
        l -= 1
print(ans)
```



代码运行截图 

![image-20240403184328223](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202404031843013.png)



### 27932: Less or Equal

http://cs101.openjudge.cn/practice/27932/



思路：直觉告诉我首尾可能有特殊情况，分开讨论即可



代码

```python
n, k = map(int, input().split())
ls = sorted(list(map(int, input().split())))
if k == n:
    print(ls[-1])
elif k == 0:
    print(1 if ls[0] != 1 else -1)
else:
    print(ls[k - 1] if ls[k - 1] != ls[k] else -1)
```



代码运行截图 

![image-20240403184352885](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202404031843103.png)



### 27948: FBI树

http://cs101.openjudge.cn/practice/27948/



思路：自定义类+递归



代码

```python
def s_type(s):
    if '1' not in s:
        return 'B'
    elif '0' not in s:
        return 'I'
    else:
        return 'F'


class Tree:
    def __init__(self):
        self.t = ''
        self.left = self.right = None

    def build_tree(self, s):
        self.t = s_type(s)

        if len(s) == 1:
            return
        else:
            mid = len(s) // 2
            self.left = Tree()
            self.right = Tree()
            self.left.build_tree(s[:mid])
            self.right.build_tree(s[mid:])

    def __str__(self):
        if self.left:
            return str(self.left) + str(self.right) + self.t
        else:
            return self.t


input()
s = input()
tree = Tree()
tree.build_tree(s)
print(tree)
```



代码运行截图 

![image-20240403184408143](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202404031844528.png)



### 27925: 小组队列

http://cs101.openjudge.cn/practice/27925/



思路：看了提交同学的内存占用，很小，干脆不弹出空列表了，记录队首位置即可



代码

```python
from queue import Queue

t = int(input())
groups = {}
search = {}
for i in range(t):
    ls = list(map(int, input().split()))
    groups[i] = ls
    for j in ls:
        search[j] = i
q = []
start = 0
l = 0
groups_in = {i: -1 for i in range(t)}

while True:
    s = input().split()
    if s[0][0] == 'S':
        break
    elif s[0][0] == 'D':
        print(q[start].get())
        if q[start].empty() == 1:
            start += 1
            l -= 1
    else:
        num = int(s[1])
        idx = search[num]
        i = groups_in[idx]
        if i - start >= 0:
            q[i].put(num)
        else:
            groups_in[idx] = start + l
            q.append(Queue())
            q[-1].put(num)
            l += 1
```



代码运行截图 

![image-20240403184438951](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202404031844318.png)



### 27928: 遍历树

http://cs101.openjudge.cn/practice/27928/



思路：建树麻烦，直接递归了



代码

```python
dic = {}
n = int(input())
for _ in range(n):
    ls = list(map(int, input().split()))
    dic[ls[0]] = ls[1:]
roots = {i: True for i in dic}
for i in dic:
    for j in dic[i]:
        roots[j] = False
for i in roots:
    if roots[i]:
        root = i
        break


def iterate(i):
    ls = sorted([i] + dic[i])
    for j in ls:
        if i == j:
            print(i)
        else:
            iterate(j)


iterate(root)
```



代码运行截图 

![image-20240403184458315](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202404031844782.png)



## 2. 学习总结和收获

​	月考题目蛮简单的，45min一遍过，不写诗了，补一补每日选做吧。
