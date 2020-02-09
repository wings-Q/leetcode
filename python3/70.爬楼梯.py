#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        for i in range(n-1):
            c = a+b
            a = b
            b = c
        return a
# @lc code=end

print(Solution.climbStairs(1,28))