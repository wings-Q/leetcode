#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        return str(bin(a+b))[2:] if str(bin(a+b))[0:1] != '-' else '-'+str(bin(a+b))[3:]
# @lc code=end

