#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        L = []
        i = 0
        w = 10
        y = 0
        uni = False
        if x<0:
            x = -x
            uni = True
        while True:
            L.append(x%w)
            x = (x - L[i])/10
            i = i + 1
            if x < 0.5:
                break
        for l in L:
            y = y*10 + l
        if uni:
            y = -y
        if y<-2**31 or y>2**31-1:
            return 0
        else:
            return int(y)

# @lc code=end
