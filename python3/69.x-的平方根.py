#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        a = x/3 if x/3>=1 else 1
        b = 0
        while abs(a-b)>=1:
            b = a
            a = (a + x/a)/2
        return int(a)
# @lc code=end

