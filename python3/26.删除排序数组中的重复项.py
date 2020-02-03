#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        for num in nums:
            if num != nums[i]:
                i = i+1
                nums[i] = num
        print(nums)
        return i+1


# @lc code=end
print(Solution.removeDuplicates(1,[0,0,1,1,1,2,2,2,3,3,4,4,5]))
