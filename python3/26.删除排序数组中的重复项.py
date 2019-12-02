#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums) -> int:
        prenum = nums[0]
        for n,num in nums[1:]:
            if num == prenum:
                nums.pop
        return len(set(nums))


# @lc code=end
print(Solution.removeDuplicates(1,[1,1,2]))
