"""
Flatten a nested list.

Answer: Use recursion or iterative stack.

Test: [1,[2,[3,4]],5] → [1,2,3,4,5]
"""

def flat(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flat(item))
        else:
            flat_list.append(item)
    return flat_list

arr = [1,[2,[3,4]],5]
print(flat(arr))