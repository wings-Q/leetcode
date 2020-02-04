#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums) -> int:
        i = 1
        for n in nums[1:]:
            if nums[i-1]>0:
                nums[i] = nums[i]+nums[i-1]
            i = i+1
        return max(nums)
# @lc code=end
print(Solution.maxSubArray(1,[-2,1,-3,4,-1,2,1,-5,4]))
