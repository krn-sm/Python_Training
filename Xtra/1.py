"""
Check if number is power of two.
Answer: n>0 and n&(n-1)==0.
Test: 16→True, 18→False
"""
def is_power2(n):
    if n > 0 and (n & n-1) == 0:
        return True
    else:
        return False
print(is_power2(246))