
# Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.

# If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".

# The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

# For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.
 

# Example 1:

# Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# Output: ["/a","/c/d","/c/f"]
# Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
# Example 2:

# Input: folder = ["/a","/a/b/c","/a/b/d"]
# Output: ["/a"]
# Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".
# Example 3:

# Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
# Output: ["/a/b/c","/a/b/ca","/a/b/d"]

from typing import List
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the folders to ensure that parent folders come before subfolders
        folder_set = set(folder)
        result = []

        for path in folder:
                result.append(path)
                for i in range(len(path)):
                    #  for each / in path we check the subset leading before the / and if it already exists then we know it is a subfolder and should not be added
                    # example if we are testing /a/b/c we check / and path[:i] == null so continue
                    #  we then check / before b and path[:i] = "a/b" if this is in fodler_set then we know its subfolder and shoulnt be added
                    #  we then check / before c and path[:i] = a/b/c same thing
                     if path[i] == "/" and path[:i] in folder_set:
                        result.pop()
                        break

        return result

sol = Solution()
print(sol.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))







# from typing import List
# class Solution:
#     def removeSubfolders(self, folder: List[str]) -> List[str]:
#         # Sort the folders to ensure that parent folders come before subfolders
#         folder.sort()
#         result = []

#         for path in folder:
#             # If result is empty or the current path is not a subfolder of the last added path
#             if len(result) == 0 or path.startswith(result[-1] + '/') == False:
#                 result.append(path)

#         return result

# sol = Solution()
# print(sol.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))