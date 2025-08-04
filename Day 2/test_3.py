"""
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits
It should only contain alphanumeric characters
No character should repeat.
There must be exactly 10 characters in a valid UID.
"""



def isvalid(id):
    if len(id)!=10 or len(set(id)) != 10 or not id.isalnum():
        return False
    count1 = sum(1 for i in id if i.isupper())
    count2 = sum(1 for j in id if j.isdigit())
    if count1 < 2 or count2 < 3:
        return False
    return True
T = int(input())
for i in range(T):
    id = input()
    print("Valid" if isvalid(id) else "Invalid")