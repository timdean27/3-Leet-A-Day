from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(current: str, open_count: int, close_count: int):
            # If the current string has reached the maximum length, add it to the results
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Add an opening parenthesis if we still have some left
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            
            # Add a closing parenthesis if it won't violate the well-formed condition
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        result = []
        backtrack("", 0, 0)
        return result
