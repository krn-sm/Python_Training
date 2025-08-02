"""
Given a list of numbers from 0 to n-1, with n elements, exactly one element is missing.
Determine the missing element.
"""

def missing(arr):
    n = len(arr)+1
    sum_of_n = (n-1)*(n) // 2
    sum_of_arr = sum(arr)
    return sum_of_n - sum_of_arr
arr = list(map(int, input("Enter the elements: ").split(" ")))
print("The missing number is ",missing(arr))