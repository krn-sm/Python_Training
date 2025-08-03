"""
Find middle node of a linked list.
Answer: Floyd’s tortoise and hare.
Test: [1,2,3,4,5] → 3
"""

class Node:
        def __init__(self, val):
                 self.val = val
                 self.next = None

def find_middle_node(head):
    slow = head  # Tortoise: moves one step
    fast = head  # Hare: moves two steps
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # Slow will be at the middle when fast reaches end

# Helper function to build linked list from a list
def build_linked_list(values):
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

# Test input
values = [1, 2, 3, 4, 5]
head = build_linked_list(values)

print("Original Linked List:")
print_linked_list(head)

# Find and print the middle node
middle = find_middle_node(head)
print("Middle Node Value:", middle.val)