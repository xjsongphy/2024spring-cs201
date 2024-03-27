"""于2024-3-19测试通过"""
from math import factorial
n = int(input())
print(factorial(2 * n) // (factorial(n))**2 // (n + 1))