// Given an array nums of size n, return the majority element.

// The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

// Example 1:

// Input: nums = [3,2,3]
// Output: 3
// Example 2:

// Input: nums = [2,2,1,1,1,2,2]
// Output: 2

var majorityElement = function (nums) {
  let hash = {};
  let largestElement = 0;
  let lengthlargestElement = 0
  for (let i = 0; i < nums.length; i++) {
    //if hash already exists push nums[i] into key
    if (hash[nums[i]]) {
      hash[nums[i]].push(nums[i]);
    }
    //else if hash does not exist set hash name with nums[i] = to nums[i]
    else {
      hash[nums[i]] = [nums[i]];
    }
  }
  let values = Object.values(hash);
  //gets values of the hashes
  console.log("values", values.length);
  for (let j = 0; j < values.length; j++) {
    console.log("value", values[j].length, values[j]);
    if (values[j].length >= lengthlargestElement) {
      console.log("values[j][0]", values[j][0]);
      largestElement = values[j][0];
      lengthlargestElement = values[j].length
    }
    console.log("largestElement",largestElement)
  }
  return largestElement;
};

console.log(majorityElement([-1, 1, 1, 1, 2, 1]));
