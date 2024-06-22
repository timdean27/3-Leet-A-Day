# // You are given an integer array height of length n. 
# // There are n vertical lines drawn such that 
# // the two endpoints of the ith line are (i, 0) 
# // and (i, height[i]).

# // Find two lines that together with the x-axis 
# // form a container, such that the container contains 
# // the most water.

# // Return the maximum amount of water a container can store.

# // Notice that you may not slant the container.

 

# // Example 1:


# // Input: height = [1,8,6,2,5,4,8,3,7]
# // Output: 49
# // Explanation: The above vertical lines are represented by 
# // array [1,8,6,2,5,4,8,3,7]. In this case,
# //  the max area of water (blue section) the container 
# //  can contain is 49.


# // find the hiegst left and heighest right and 
# //check if the distance between makes the area larger


from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        largestLeft = 0
        largestRight = len(height) - 1
        maxArea = 0

        while largestLeft < largestRight:
            distance = largestRight - largestLeft
            currentArea = min(height[largestLeft], height[largestRight]) * distance
            maxArea = max(maxArea, currentArea)

            if height[largestLeft] < height[largestRight]:
                largestLeft += 1
            else:
                largestRight -= 1
        
        return maxArea
