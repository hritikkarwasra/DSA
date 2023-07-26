# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

class Solution:
    def helper(self, ans, curr, i, nums):
        if i >= len(nums):
            # print(curr)
            return ans.append(curr.copy())

        curr.append(nums[i])
        self.helper(ans, curr, i+1, nums)
        curr.pop()
        self.helper(ans, curr, i+1, nums)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.helper(ans, [], 0, nums)
        
        return sorted(ans)