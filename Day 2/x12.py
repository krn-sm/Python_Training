"""
Implement binary search.​
Classic mid-pointer search.​
"""

def binary_search(arr, target):
    left, right = 0, len(arr)
    while left <= right:
        mid = (left + right)// 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1



arr = [1, 2, 3, 4, 5, 6]
target = 8
binary_search(arr, target)
