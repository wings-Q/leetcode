#
# @lc app=leetcode.cn id=7 lang=python3
# [7] 整数反转
#
'''
# @lc code=start

class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        uni = False
        if x<0:
            x = -x
            uni = True
        while True:
            a = x%10
            x = (x - a)/10
            y = y*10+a
            if x < 0.5:
                break
        if uni:
            y = -y
        if -2147483647<y<2147483648:
            return int(y)
        else:
            return 0

# @lc code=end

m = Solution.reverse(1,-100)
print(m)
'''

# @lc code=start

class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        uni = False
        if x<0:
            x = -x
            uni = True
        stringx = str(x)[::-1]
        y = int(stringx)
        if uni:
            y = -y
        if 2147483647<y<-2147483648:
            return 0
        else:    
            return y

# @lc code=end

m = Solution.reverse(1,-100)
print(m)