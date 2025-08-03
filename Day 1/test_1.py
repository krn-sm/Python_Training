"""Luffy is participating in a numbers game. He is given a array of n numbers and have to find if the array of numbers is flawless.
An array of numbers is considered flawless if and only if for every pair of elements ai,aj ; i != j there exists an element ak such that ak = ai * aj. 
Where k can also be equal to i or j.
Find out if the given array of numbers is flawless.

Input Format
First line of the input contains an integer T denoting the number of test cases. T test cases follow.
First line of each test case contains an integer n denoting number of elements in the array.
Next line contains n space separated integers denoting the array elements.

Constraints
1 <= T <= 10^9
2 <= n <= 10^9
-10^9 ≤ ai ≤ 10^9
Output Format

For each test case, output a single line containing "yes" or "no" (without quotes) corresponding to the answer of the problem
"""

T = int(input())
for test in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    flag = False
    s = set(arr)
    for i in range(n):
        for j in range(n):
            if i != j:
                if arr[i] * arr[j] not in s:
                    print("no")
                    flag = True
                    break
        if flag:
            break
    else:
        print("yes")




