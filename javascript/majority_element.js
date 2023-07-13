// Given an array nums of size n, return the majority element.

// The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

// Example 1:

// Input: nums = [3,2,3]
// Output: 3
// Example 2:

// Input: nums = [2,2,1,1,1,2,2]
// Output: 2
 

// Constraints:

// n == nums.length
// 1 <= n <= 5 * 104
// -109 <= nums[i] <= 109
// //  

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    var counter = 0;
    const n = nums.length;
    var ele;
    if (n < 2) return nums[0];

    for(let i = 0; i < n; i++){
        if (counter > Math.floor(n/2)) return ele;
        if (counter == 0){
            counter = 1;
            ele = nums[i];
        }
        else if(nums[i] == ele) counter++;
        else counter--;
    }
    return ele
};