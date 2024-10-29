# 206. Reverse Linked List
# Solved
# Easy
# Topics
# Companies
# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next  # Store the next node
            current.next = prev       # Reverse the link
            prev = current            # Move prev to current
            current = next_node       # Move to the next node

        return prev  # New head of the reversed linked list
    
    # example 1-2-3-4-5
    # FIRST
    # next_node = 2
    # current.next = none
    # prev = 1
    # current = 2
    # SECOND
    # next_node = 3 because current is 2 and nextis 3
    # current.next = 1
    # prev = 2
    # current = 3
    # THIRD
    # next_node = 4 because current is 3 and nextis 4
    # current.next = 2
    # prev = 3
    # current = 4

def print_linked_list(head: ListNode):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original Linked List:")
print_linked_list(head)

# Reverse the linked list
solution = Solution()  # Create an instance of the Solution class
reversed_head = solution.reverseList(head)

print("Reversed Linked List:")
print_linked_list(reversed_head)
