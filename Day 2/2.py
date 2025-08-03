"""
Check if two strings are anagrams
Answer: Sort both or count frequencies.

Test: "listen", "silent" → True
"""
string1 = input("Enter the first string: ").lower()
string2 = input("Enter the second string: ").lower()
print(sorted(string1) == sorted(string2))
