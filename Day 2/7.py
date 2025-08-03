"""
Check if parentheses string is valid. 
Answer: Use stack and matching pairs.
Test: "([])" → True, "(]" → False
"""
def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack


par1 = "([])"
par2 = "(]"
print(is_valid_parentheses(par1))  # Output: True
print(is_valid_parentheses(par2))  # Output: False
