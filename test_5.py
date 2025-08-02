"""
Given a integer n, print all the number numbers from 1 upto (including) n.

Input Format
A single integer n

Constraints
1 <= n <= 10^9

Output Format
A single line output of space separated integers(primes)
"""
def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
n = int(input())
result = ""
for i in range(1, n+1):
    if isprime(i):
        result += str(i) + " "
print(result.strip())
