# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # creat an object to match opening brackets with closing
        bracket_object = {'(': ')', '{': '}', '[': ']'}

        for i in range(len(s)):
            if s[i] in bracket_object:  # If it's an opening bracket
                stack.append(s[i])
            else:  # It's a closing bracket
                if not stack:  # Check if stack is empty , if empty we hit a closing bracket before adding any open
                    return False
                # pop will remove the stack indexed at the end stack[len(stack)-1]
                top_element = stack.pop() 
                # Check if the popped element matches the closing bracket
                # if the current closing bracket s[i] does not match the open bracket at the end of stack then we do not close properly 
                if bracket_object[top_element] != s[i]:
                    return False

        return len(stack) == 0  # Check if all opening brackets are matched


sol = Solution()
print(sol.isValid("()"))         # Output: True
print(sol.isValid("()[]{}"))     # Output: True
print(sol.isValid("(]"))         # Output: False
print(sol.isValid("([)]"))       # Output: False
print(sol.isValid("{[]}"))       # Output: True
