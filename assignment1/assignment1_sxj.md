# Assignment #1: 拉齐大家Python水平

Updated 0940 GMT+8 Feb 19, 2024

2023 fall, Complied by Xinjie Song, Phy



**说明：**

1）数算课程的先修课是计概，由于计概学习中可能使用了不同的编程语言，而数算课程要求Python语言，因此第一周作业练习Python编程。如果有同学坚持使用C/C++，也可以，但是建议也要会Python语言。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知3月1日导入选课名单后启用。**作业写好后，保留在自己手中，待3月1日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**


操作系统：Windows 11 22H2

Python编程环境：PyCharm 2023.2 (Community Edition)

C/C++编程环境：g++ (x86_64-win32-seh-rev0, Built by MinGW-W64 project) 8.1.0



## 1. 题目

### 20742: 泰波拿契數

http://cs101.openjudge.cn/practice/20742/



思路：善用Python负数索引



##### 代码

```python
ls = [0, 1, 1]
for i in range(30):
    ls.append(ls[-1] + ls[-2] + ls[-3])
print(ls[int(input())])
```



代码运行截图 

![image-20240219161613645](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202402191616762.png)



### 58A. Chat room

greedy/strings, 1000, http://codeforces.com/problemset/problem/58/A



思路：常规思路



##### 代码

```python
str_input = input()
str_wanted = 'hello'
 
yes_or_no = True
 
for i in range(0, len(str_wanted)):
    if str_wanted[i] in str_input:
        index = str_input.find(str_wanted[i])
 
        if index == len(str_input) - 1:
            str_input = ''
        else:
            str_input = str_input[index + 1:]
    else:
        yes_or_no = False
        break
 
if yes_or_no:
    print('YES')
else:
    print('NO')
```



代码运行截图 

![image-20240219161718786](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202402191617922.png)



### 118A. String Task

implementation/strings, 1000, http://codeforces.com/problemset/problem/118/A



思路：常规思路



##### 代码

```python
output_list = []
input_list = list(input().lower())
string_for_search = 'aoyeui'
 
for char in input_list:
    if char in string_for_search:
        continue
    else:
        output_list.append('.')
        output_list.append(char)
 
print(''.join(output_list))
```



代码运行截图 

![image-20240219161745950](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202402191617112.png)



### 22359: Goldbach Conjecture

http://cs101.openjudge.cn/practice/22359/



思路：直接从cheatsheet上抄欧拉筛



##### 代码

```python
n = int(input())
nums = {i: True for i in range(2, n)}
primes = []

for i in range(2, n):
    if nums[i]:
        primes.append(i)
    for j in primes:
        if i*j >= n:
            break
        nums[i*j] = 0
        if i % j == 0:
            break

dic = {i: True for i in primes}
for prime in primes:
    if n - prime in dic:
        print(prime, n - prime)
        break
```



代码运行截图 

![image-20240219162214285](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202402191622389.png)



### 23563: 多项式时间复杂度

http://cs101.openjudge.cn/practice/23563/



思路：善用正则表达式



##### 代码

```python
from re import match

ls = [i.split('^') for i in input().split('+')]
max_num = 0
for i in ls:
    if match(rf'[0-9]+', i[-1]):
        if i[0][0] != '0' and int(i[-1]) > max_num:
            max_num = int(i[-1])
print(f'n^{max_num}')
```



代码运行截图 

![image-20240219162255279](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202402191622423.png)



### 24684: 直播计票

http://cs101.openjudge.cn/practice/24684/



思路：字典快速查找计数，转成元组的列表排序



##### 代码

```python
ls = list(map(int, input().split()))
dic = {i: 0 for i in set(ls)}
for i in ls:
    dic[i] += 1

ls = sorted([(-v, k) for k, v in dic.items()])
c = ls[0][0]
print(ls[0][1], end='')
for i in ls[1:]:
    if i[0] > c:
        break
    print(f' {i[1]}', end='')
```



代码运行截图 

![](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202402191632551.png)



## 2. 学习总结和收获

​	题目过于简单；至于额外题目，刚开学，先不练了。





