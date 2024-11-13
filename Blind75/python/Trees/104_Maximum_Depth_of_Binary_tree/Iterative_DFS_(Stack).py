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
        # Initialize queue to hold nodes at each level
        if not root:
                    return 0
                
        stack = [[root, 1]]  # Start with the root node and depth 1
        res = 0  # Result to keep track of maximum depth
        
        while stack:
            node, depth = stack.pop()  # Pop the top item from the stack
            print(f"Popped node: {node.val if node else 'None'}, depth: {depth}")

            if node:
                # Update the maximum depth
                res = max(res, depth)
                print(f"Updated maximum depth to: {res}")

                # Add the left and right children to the stack with incremented depth
                if node.left:
                    stack.append([node.left, depth + 1])
                    print(f"Added left child {node.left.val} with depth {depth + 1} to stack")
                if node.right:
                    stack.append([node.right, depth + 1])
                    print(f"Added right child {node.right.val} with depth {depth + 1} to stack")

        
        return res

# Example usage
root_values = [1, 2, 3, None, None, 4]
root = build_tree_from_list(root_values)
solution = Solution()
max_depth = solution.maxDepth(root)

print(f"Maximum depth of the tree: {max_depth}")



### Explanation of the Process with the Tree `root = [1, 2, 3, None, None, 4]`

# Given the tree structure:
# ```
#         1
#        / \
#       2   3
#            \
#             4
# ```

# This representation corresponds to:
# - `root` node: `1`
# - `root.left`: `2`
# - `root.right`: `3`
# - `root.right.right`: `4`

# ### Step-by-Step Walkthrough with Print Output

# 1. **Initialization**:
#    - `stack = [[root, 1]]` where `root` is node `1` (so `[1, 1]`).
#    - `res = 0`.

# 2. **First Iteration**:
#    - `stack.pop()` gives `node = 1` and `depth = 1`.
#    - Print: `Popped node: 1, depth: 1`.
#    - Update `res = max(res, depth)`, so `res = 1`.
#    - Print: `Updated maximum depth to: 1`.
#    - Push left and right children:
#      - `stack.append([2, 2])` for the left child `2`.
#      - Print: `Added left child 2 with depth 2 to stack`.
#      - `stack.append([3, 2])` for the right child `3`.
#      - Print: `Added right child 3 with depth 2 to stack`.

#    **Stack after this iteration**: `[[2, 2], [3, 2]]`.

# 3. **Second Iteration**:
#    - `stack.pop()` gives `node = 3` and `depth = 2`.
#    - Print: `Popped node: 3, depth: 2`.
#    - Update `res = max(res, depth)`, so `res = 2`.
#    - Print: `Updated maximum depth to: 2`.
#    - Push left and right children:
#      - `stack.append([4, 3])` for the right child `4`.
#      - Print: `Added right child 4 with depth 3 to stack`.

#    **Stack after this iteration**: `[[2, 2], [4, 3]]`.

# 4. **Third Iteration**:
#    - `stack.pop()` gives `node = 4` and `depth = 3`.
#    - Print: `Popped node: 4, depth: 3`.
#    - Update `res = max(res, depth)`, so `res = 3`.
#    - Print: `Updated maximum depth to: 3`.
#    - Node `4` has no children, so nothing is added to the stack.

#    **Stack after this iteration**: `[[2, 2]]`.

# 5. **Fourth Iteration**:
#    - `stack.pop()` gives `node = 2` and `depth = 2`.
#    - Print: `Popped node: 2, depth: 2`.
#    - Update `res = max(res, depth)`, so `res` remains `3`.
#    - Node `2` has no children, so nothing is added to the stack.

#    **Stack after this iteration**: `[]`.

# 6. **Termination**:
#    - The stack is now empty, so we exit the `while` loop.
#    - The maximum depth found is `3`.

# ### Final Output

# The function returns `3`, which is the maximum depth of the tree.

# ### Summary of Print Statements Output

# # Popped node: 1, depth: 1
# Updated maximum depth to: 1
# Added left child 2 with depth 2 to stack
# Added right child 3 with depth 2 to stack
# Popped node: 3, depth: 2
# Updated maximum depth to: 2
# Added right child 4 with depth 3 to stack
# Popped node: 4, depth: 3
# Updated maximum depth to: 3
# Popped node: 2, depth: 2
# ```

# This provides a clear view of how the function progresses through each node in the stack, updating the maximum depth as it encounters nodes at greater depths.