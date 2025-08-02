"""
Given a list of numbers from 0 to n-1,
for n+1 elements in a list, exactly one element is duplicated.
determine the duplicated number.
"""

def duplicate(arr):
    n = len(arr)
    sum_of_n = (n-1)*(n-2) // 2   #sum of first n natural numbers = n*(n+1)/2
    sum_of_arr = sum(arr)        #sum of first n whole numbers = n*(n-1)/2
    return sum_of_arr - sum_of_n
arr = list(map(int, input("Enter the elements: ").split(" ")))
print("The duplicate number is ",duplicate(arr))