"""
A valid mobile number is a ten digit number starting with a  or 7, 8, or 9.
Input Format
The first line contains an integer N the number of inputs.
N lines follow, each containing some string.
Output Format
For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.
"""

n = int(input())
for i in range(n):
    number = input() 
    if len(number)==10 and number.isdigit() and number[0] in '789':
        print("YES")
    else:
        print("NO")