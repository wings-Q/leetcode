#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1
        while numbers[left]+numbers[right] != target:
            if numbers[left]+numbers[right] > target:
                right -= 1
            else:
                left +=1
        return [left+1,right+1]

# @lc code=end

