#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        k = 0
        for num in nums2:
            while num > nums1[i] and i<m+k:
                i = i+1
            nums1.insert(i,num)
            nums1.pop(-1)
            k = k+1
# @lc code=end