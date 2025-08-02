"""
Write a Python program to check whether a given number is a palindrome (same when read forward and backward).
Input Format

A single integer n denoting the number
Constraints
1 < n < 10^12

Output Format
A single string 'Palindrome' or 'Not Palindrome' indicating whether the given number of is a palindrome.
"""

n = input().strip()
if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")