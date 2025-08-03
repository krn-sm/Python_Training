"""
Merge two sorted lists.
Answer: Two-pointer merge in O(n+m).
Test: [1,3,5], [2,4] → [1,2,3,4,5]
"""

l1 = [1,3,5]
l2 = [2,4]
merged_list = []
i = j =0
while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
        merged_list.append(l1[i])
        i += 1
    else:
        merged_list.append(l2[j])
        j += 1
print(merged_list + l1[i:] + l2[j:])