"""
Jesse loves cookies and wants the sweetness of some cookies to be greater than value k. 
To do this, two cookies with the least sweetness are repeatedly mixed. 
This creates a special combined cookie with:

sweetness = (1 * Least sweet cookie  + 2 * 2nd least sweet cookie).

This occurs until all the cookies have a sweetness >= k
Given the sweetness of a number of cookies, determine the minimum number of operations required. If it is not possible, return -1
"""

import heapq
def cookies(k, A):
    heapq.heapify(A)
    count = 0
    
    while len(A) >= 2 and A[0] < k:
        first = heapq.heappop(A)
        second = heapq.heappop(A)
        new_cookie = first + 2 * second
        heapq.heappush(A, new_cookie)
        count += 1
        
    return count if A and A[0] >= k else -1

A = [1, 2, 3, 9, 10, 12]
k = 7
print(cookies(k, A))  


