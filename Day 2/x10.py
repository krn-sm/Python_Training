"""
Sort characters by frequency.​
"""

from collections import Counter
def freq_sort(s):
    freq = Counter(s)
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    result = ''.join(char * count for char, count in freq)
    return result
s = "tree"
print(freq_sort(s))