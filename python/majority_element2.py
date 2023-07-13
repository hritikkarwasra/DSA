# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1, cnt2, ele1, ele2 = 0, 0, None, None
        ans = []
        for i in nums:
            if cnt1 == 0 and ele2!= i: 
                cnt1 =1 
                ele1 = i
            elif cnt2 == 0 and ele1!= i:
                cnt2 = 1
                ele2 = i
            elif ele1 == i:
                cnt1 +=1
            elif ele2 == i:
                cnt2 +=1
            else:
                cnt1-=1
                cnt2-=1
        cnt1, cnt2 = 0, 0
        for i in nums:
            if i == ele1:
                cnt1+=1
            elif i == ele2:
                cnt2+=1
        
        if cnt1 > len(nums)//3:
            ans.append(ele1)
        if cnt2 > len(nums)//3:
            ans.append(ele2)

        return ans