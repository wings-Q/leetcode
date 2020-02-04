#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        for n in nums:
            if n >= target:
                return i
            i = i+1
        return i
# @lc code=end

