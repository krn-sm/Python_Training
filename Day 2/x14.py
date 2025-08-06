"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""

arr = [3,0,1]
sum_of_n = sum(range(len(arr) + 1))
sum_of_arr = sum(arr)
missing_number = sum_of_n - sum_of_arr
print(missing_number)