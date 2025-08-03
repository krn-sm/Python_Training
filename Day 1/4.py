"""
Write a program to find the length of longest sub string 
of a given string which contains exactly k unique characters.
"""

def substring(s, k):
    i, j = 0, 1
    length = 0
    while i < len(s) and j <= len(s) and i <= j: 
        Uni_char = len(set(s[i:j]))
        if Uni_char == k:
            length = max(length, j - i)
            j+= 1
        elif Uni_char < k:
            j += 1
        else:
            i += 1 
    return length
        
s = input("Enter the string: ")
k = int(input("Enter the number of unique characters: "))
print("The longest substring with exactly", k, "unique characters is of length", substring(s, k))


''' 
def substring(s, k):
    n = len(s)
    length = 0 
    for i in range(n):
        char = set()
        for j in range(i, n):
            char.add(s[j])
            if len(char) == k:
                    length = max(length, j - i + 1)
            elif len(char) > k:
                    break
    return length
   '''
'''
def substring(s, k):
    n = len(s)
    length = 0 
    char_count = {}
    left = 0
    for right in range(n):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        length = max(length, right - left + 1)
    return length
'''