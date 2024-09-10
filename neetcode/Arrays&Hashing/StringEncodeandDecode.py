# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            # loop through strs array
            count = len(string)
            encoded_string += str(count) + "#" + string
            # at the start of each element in the array we add the length of the string and a # so we know when we hit a # we will want the vlaues count amount following 
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        # innitiat an array and an index at 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                # start when value in s is not # and continue until hitting the #
                j += 1
                # we dont want to inclued the # at start
            length = int(s[i:j])

            result.append(s[j + 1 : j + 1 + length])
            # Extract the substring using the length found j value is # so start j+1 and go to j+1 + length of string we want
            i = j + 1 + length
            # Move the index to the start of the next encoded string
        return result

sol = Solution()
encoded_ans = sol.encode(["neet", "code", "love", "you"])
print(encoded_ans)
decoded_ans = sol.decode(encoded_ans)
print(decoded_ans)

