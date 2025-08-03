"""
Count unique characters in a string
Answer: Use a set or collections.Counter to count unique chars.
Test: "hello" → 4
"""

string = input("Enter a string: ")
print("The number of unique characters is:", len(set(string)))