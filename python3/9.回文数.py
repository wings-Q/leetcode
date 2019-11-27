#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        if strx == strx[::-1]:
            return True
        else:
            return False
# @lc code=end

