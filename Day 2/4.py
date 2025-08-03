"""
Find duplicates in a list.
Answer: Use set to track seen and duplicates list.

Test: [1,2,3,2,4,3] → [2,3]
"""
# arr = list(map(int, input("Enter the elements of the array: ").split(',')))
# seen = set()
# duplicates = []
# for i in arr:
#     if i in seen:
#         duplicates.append(i)
#     else:
#         seen.add(i)
# print(duplicates)


from collections import Counter
x = [1,2,3,2,4,3]
print([num for num,val in Counter(x).items() if val>1])
