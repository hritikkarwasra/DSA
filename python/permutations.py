# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def generate(nums, path):
            print("path:", path)
            if not nums:
                ans.append(path)
                print('appending to ans:', path)
            for i in range(len(nums)):
                print(f"i ={i}")
                print("nums[:i] :", nums[:i])
                print("nums[i+1:] :", nums[i+1:])
                generate(nums[:i] + nums[i+1:], path+ [nums[i]])
        ans =[]
        generate(nums, [])
        return ans