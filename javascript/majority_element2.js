// Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

// Example 1:

// Input: nums = [3,2,3]
// Output: [3]
// Example 2:

// Input: nums = [1]
// Output: [1]
// Example 3:

// Input: nums = [1,2]
// Output: [1,2]

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
    var cnt1 = 0;
    var cnt2 =  0;
    var ele1;
    var ele2;
    let arr = []

    for(let i = 0; i < nums.length ; i++){
        if(cnt1 == 0 && ele2 != nums[i]){
            cnt1= 1;
            ele1= nums[i];
        }
        if(cnt2 == 0 && ele1 != nums[i]){
            cnt2 = 1;
            ele2 = nums[i];
        }
        else if (ele1 == nums[i]) cnt1++;
        else if (ele2 == nums[i]) cnt2++;
        else{
            cnt1--; cnt2--;
        }
    }
    cnt1 = 0;
    cnt2 = 0;
    for(let i = 0 ; i < nums.length ; i++){
        if(nums[i]== ele1)  cnt1++;
        if(nums[i] == ele2) cnt2++;
    }
    if (cnt1 >= Math.floor(nums.length/3)+1) arr.push(ele1);
    if (cnt2 >= Math.floor(nums.length/3)+1) arr.push(ele2);

    return arr;
};