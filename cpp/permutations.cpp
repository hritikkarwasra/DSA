// Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

// Example 1:

// Input: nums = [1,2,3]
// Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
// Example 2:

// Input: nums = [0,1]
// Output: [[0,1],[1,0]]
// Example 3:

// Input: nums = [1]
// Output: [[1]]

class Solution {
public:
    void helper(int ind, vector<vector<int>> &ans, vector<int>&nums){
        if(ind == nums.size()){
            ans.push_back(nums);
            return;
        }
        for(int i = ind ; i <nums.size(); i++){
            swap(nums[i], nums[ind]);
            helper(ind +1 , ans , nums);
            swap(nums[i], nums[ind]);
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>>ans;
        helper(0, ans, nums);
        sort(ans.begin(), ans.end());
        return ans;
    }
};