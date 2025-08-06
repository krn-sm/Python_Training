"""
Mr. Ramesh is the manager at the hotel. The hotel has an infinite amount of rooms.
One fine day, a number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of members per group where ≠ .
The Captain was given a separate room, and the rest were given one room per group.
Mr. Ramesh has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear times per group except for the Captain's room.
Mr. Ramesh needs you to help him find the Captain's room number.


The first line consists of an integer, , the size of each group.
The second line contains the unordered elements of the room number list.

Output the Captain's room number.
"""
from collections import Counter
def room(n, rooms):
    count = Counter(rooms)
    for i, freq in count.items():
        if freq != n:
            return i
n = int(input())
rooms = list(map(int, input().split()))
print(room(n, rooms))





