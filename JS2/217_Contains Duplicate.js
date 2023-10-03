// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

// Example 1:

// Input: nums = [1,2,3,1]
// Output: true
// Example 2:

// Input: nums = [1,2,3,4]
// Output: false
// Example 3:

// Input: nums = [1,1,1,3,3,4,3,2,4,2]
// Output: true


var containsDuplicate = function(nums) {
   // Create an empty Set to store unique elements
   const uniqueElements = new Set();
//    Uniqueness: Sets ensure that each element appears only once. If you attempt to add a duplicate element to a set, it will not be added.
//    No Specific Order: Sets do not guarantee any specific order for their elements. Elements are typically stored in an unordered manner.
//    Adding Elements: You can add elements to a set using the add method.
//    Removing Elements: You can remove elements from a set using the delete method.
   
//    Checking Membership: You can check if an element exists in a set using the has method.
   for (let i = 0 ; i < nums.length; i++) {
       // If the current element is already in the Set, return true
       if (uniqueElements.has(nums[i])) {
           return true;
       }
       // Otherwise, add it to the Set
       else {
           uniqueElements.add(nums[i]);
       }
   }
   
   // If no duplicates were found, return false
   return false;
}
    


console.log(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))