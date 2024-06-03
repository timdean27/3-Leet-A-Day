// You are given an integer array height of length n. 
// There are n vertical lines drawn such that 
// the two endpoints of the ith line are (i, 0) 
// and (i, height[i]).

// Find two lines that together with the x-axis 
// form a container, such that the container contains 
// the most water.

// Return the maximum amount of water a container can store.

// Notice that you may not slant the container.

 

// Example 1:


// Input: height = [1,8,6,2,5,4,8,3,7]
// Output: 49
// Explanation: The above vertical lines are represented by 
// array [1,8,6,2,5,4,8,3,7]. In this case,
//  the max area of water (blue section) the container 
//  can contain is 49.


// find the hiegst left and heighest right and 
//check if the distance between makes the area larger

var maxArea = function(height) {
    let largestLeft = 0;
    let largestRight = height.length - 1;
    let maxArea = 0;

    while (largestLeft < largestRight) {
        let distance = largestRight - largestLeft;
        let currentArea = Math.min(height[largestLeft], height[largestRight]) * distance;
        maxArea = Math.max(maxArea, currentArea);

        if (height[largestLeft] < height[largestRight]) {
            largestLeft++;
        } else {
            largestRight--;
        }
    }

    return maxArea
};

console.log(maxArea(height = [1,8,6,2,5,4,8,3,7]))