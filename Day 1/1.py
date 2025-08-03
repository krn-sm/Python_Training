"""
Count the number of valleys. 
You are given a string that represent steps in combination of U and D characters.
U represents to take a step up in level. 
D represents to take a step down in level.
You always start at sea level.
A valley is a dip from sea level and back to sea level.
"""

def solution(steps):
    level = 0
    valley = 0
    for i in steps:
        if i == 'U':
            level += 1
        else:
            level -= 1
        if level == 0 and i == 'U':  #we reached back to sea level after a valley
            valley += 1
    return valley     
steps = input("Enter the steps (U for up, D for down): ")
print("Number of valleys:",solution(steps))