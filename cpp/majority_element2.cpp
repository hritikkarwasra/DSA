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

class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> ans;
        int cnt1=0, cnt2=0, ele1, ele2;
        for(int i = 0 ; i < nums.size(); i++){
            if (cnt1== 0 && ele2 != nums[i]){
                cnt1 = 1;
                ele1 = nums[i];
            }
            else if (cnt2 == 0 && ele1!= nums[i]){
                cnt2 = 1;
                ele2 = nums[i];
            }
            else if(ele1 == nums[i]) cnt1++;
            else if(ele2 == nums[i]) cnt2++;
            else{
                cnt1--;
                cnt2--;
            }
        }
        cnt1, cnt2 = 0 , 0 ;
        for (int i = 0; i < nums.size(); i++){
            if(nums[i] == ele1) cnt1++;
            else if(nums[i]== ele2) cnt2++;
        }
        if (cnt1 >= int(nums.size()/3)+1)ans.push_back(ele1);
        if (cnt2 >= int(nums.size()/3)+1) ans.push_back(ele2);
        return ans;
    }
};