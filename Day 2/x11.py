"""
Reverse words in a sentence.​
"""

def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

#sentence = input("Enter a sentence with multiple words: ")
sentence = 'hello world'
print(reverse_words(sentence))
