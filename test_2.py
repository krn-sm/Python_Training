"""
🐐 Onam Tug of War – Pappan vs Kings Paravoor
To celebrate this year’s Onam festival, a grand Tug of War competition is being held between two legendary teams:
Pappan’s Winners (left side)
Kings Paravoor (right side)
Each team has exactly n participants, standing opposite each other in a straight line. The strength of the participants is given in alternating order:

l1 r1 l2 r2 l3 r3 ... ln rn
li is the strength of the i-th member of Pappan’s team.

ri is the strength of the i-th member of Kings Paravoor.
Before the competition begins, Pappan (who is a bit superstitious) wants to know if his team is likely to win. Your task is to help him by calculating the total strength of each side and predicting the outcome.

Input Format

The first line contains a single integer n — the number of participants on each side.

The second line contains 2n space-separated integers: l1 r1 l2 r2 ... ln rn

Constraints

1 <= n <= 1000
1 <= li <= 1000
1 <= ri <= 1000
Output Format

Print in a single line "WIN" / "LOSE" / "TIE" with respect to the outcome of the match.
"""

n = int(input())
lr = list(map(int,input().split(" ")))
flag = True
t1,t2 = 0,0

for i in range(len(lr)):
    if flag:
        t1+=lr[i]
        flag = False
    else:
        t2+=lr[i]
        flag = True
if t1>t2:
    print("WIN")
elif t2>t1:
    print("LOSE")
else:
    print("TIE")
