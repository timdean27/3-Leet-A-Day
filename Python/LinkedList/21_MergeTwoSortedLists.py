# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 # Definition for singly-linked list.



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to serve as the start of the merged list
        dummy = ListNode(0)
        current = dummy  # Pointer to the current node in the merged list

        # Traverse both lists
        while list1 and list2:  # Continue until one list is exhausted
            if list1.val < list2.val:
                current.next = list1  # Link the smaller node to the merged list
                list1 = list1.next  # Move to the next node in list1
            else:
                current.next = list2  # Link the smaller node to the merged list
                list2 = list2.next  # Move to the next node in list2
            current = current.next  # Move to the next node in the merged list

        # If there are remaining nodes in either list, append them
        if list1:
            current.next = list1  # If list1 has remaining nodes, append them
        elif list2:
            current.next = list2  # If list2 has remaining nodes, append them

        return dummy.next  # Return the merged list, skipping the dummy node

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

print("List 1:")
print_linked_list(list1)
print("List 2:")
print_linked_list(list2)

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

print("Merged List:")
print_linked_list(merged_list)
