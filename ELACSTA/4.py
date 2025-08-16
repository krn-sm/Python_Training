"""
Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

"""

n = int(input("Enter the number of elements in the array: "))
arr = []
c = 0
print("Enter the elements of the array:")
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    for j in range(i+1,n):
        if arr[i] + arr[j] in arr:
            c += 1
print(c)
