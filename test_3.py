"""
You are given three integers a,b and c, print the value of the maximum integer that can be formed using any two of these integers.
Input Format
The first and only line contains three integers a, b and c.

Constraints
0 <= a, b, c <= 1000

Output Format
A single integer representing the maximum formable value
"""

a, b, c = map(int, input().split())
max_value = max(a + b, a + c, b + c)
print(max_value)