// # Given an integer array nums of unique elements, return all possible 
// # subsets
// #  (the power set).

// # The solution set must not contain duplicate subsets. Return the solution in any order.

 

// # Example 1:

// # Input: nums = [1,2,3]
// # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
// # Example 2:

// # Input: nums = [0]
// # Output: [[],[0]]
class Solution {
public:
    vector<vector<int>> helper(vector<int>&nums, int i, vector<int> &temp, vector<vector<int>> &ans){
        if (i >= nums.size()) return ans.emplace_back(temp);

        temp.push_back(nums[i]);
        helper(nums, i+1,temp, ans);

        temp.pop_back(nums[i]);
        helper(nums, i+1, temp , ans);;
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> temp;
        vector<vector<int>> ans;

        helper(nums, 0, temp, ans);

        return ans;
    }
};