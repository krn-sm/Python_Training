"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

"""

t = input("Enter a string: ")
s = input("Enter the subseq: ")
flag = True
for i in range(len(s)):
    j = t.find(s[i])
    if j == -1:
        flag = False
    else:
        t = t[j:]
print(flag)