# Definition for a binary tree node.
from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to build a binary tree from a list
def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        current = queue.popleft()
        
        # Add left child
        if index < len(values) and values[index] is not None:
            current.left = TreeNode(values[index])
            queue.append(current.left)
        index += 1
        
        # Add right child
        if index < len(values) and values[index] is not None:
            current.right = TreeNode(values[index])
            queue.append(current.right)
        index += 1

    return root

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = []
        
        # Start with the root if it exists
        if root:
            queue.append(root)
            print(f"Starting with root node: {root.val}")

        level = 0  # Track the current depth of the tree
        
        # Process nodes level-by-level
        while queue:
            print(f"Level {level + 1} - Queue contains {[node.val for node in queue]}")
            for i in range(len(queue)):  # Loop over all nodes at the current level
                node = queue.pop(0)  # Remove the first element (front of the list)
                print(f"Popped node: {node.val}")
                
                # Add the node's children to the end of the queue if they exist
                if node.left:
                    queue.append(node.left)
                    print(f"Added left child {node.left.val} to the queue")
                if node.right:
                    queue.append(node.right)
                    print(f"Added right child {node.right.val} to the queue")
                else:
                    print(f'end of branch for node {node.val}')
            # After processing all nodes at this level, increment the level counter
            level += 1
            print(f"Completed Level {level}, current max depth is {level}")
        
        return level


# Example usage
root_values = [1, 2, 3, None, None, 4]
root = build_tree_from_list(root_values)
solution = Solution()
max_depth = solution.maxDepth(root)

print(f"Maximum depth of the tree: {max_depth}")




# Step-by-Step Explanation
# Tree Structure from List:

# From the list [1, 2, 3, None, None, 4], we can visualize the tree as:
# markdown
# Copy code
#      1
#     / \
#    2   3
#       /
#      4
# The root node is 1, which has two children: 2 (left) and 3 (right). Node 3 has a left child 4.
# Initialization:

# We start by defining our class and the maxDepth method.
# A list named queue is initialized to keep track of nodes to process.
# If the root is not None, we add it to the queue.
# The variable level is initialized to 0 to track the current depth of the tree.
# First Level (Level 1):

# Queue State: queue = [1]
# Print: Level 1 - Queue contains [1]
# We loop over the nodes in the queue (in this case, just 1):
# Popped Node: 1
# Print: Popped node: 1
# We check its children:
# Node 1 has a left child 2:
# Action: queue.append(node.left) → queue becomes [2]
# Print: Added left child 2 to the queue
# Node 1 has a right child 3:
# Action: queue.append(node.right) → queue becomes [2, 3]
# Print: Added right child 3 to the queue
# End of Level: We increment the level counter.
# Print: Completed Level 1, current max depth is 1
# Second Level (Level 2):

# Queue State: queue = [2, 3]
# Print: Level 2 - Queue contains [2, 3]
# We loop over the nodes in the queue (two nodes: 2 and 3):
# Popped Node: 2
# Print: Popped node: 2
# Node 2 has no children, so nothing is added to the queue.
# Popped Node: 3
# Print: Popped node: 3
# Node 3 has a left child 4:
# Action: queue.append(node.left) → queue becomes [4]
# Print: Added left child 4 to the queue
# Node 3 has no right child, so nothing is added to the queue.
# End of Level: We increment the level counter.
# Print: Completed Level 2, current max depth is 2
# Third Level (Level 3):

# Queue State: queue = [4]
# Print: Level 3 - Queue contains [4]
# We loop over the nodes in the queue (one node: 4):
# Popped Node: 4
# Print: Popped node: 4
# Node 4 has no children, so nothing is added to the queue.
# End of Level: We increment the level counter.
# Print: Completed Level 3, current max depth is 3
# Exit Condition:

# Now the queue is empty, so we exit the while loop.
# Return Value:

# Finally, we return the level, which is 3, representing the maximum depth of the tree.
# The final output would be:
# Print: Maximum depth of the tree: 3