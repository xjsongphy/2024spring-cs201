"""于2024-2-19测试通过"""
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