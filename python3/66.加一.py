#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits):
        rnums = [0]
        rnums.extend(digits)
        rnums[-1] = rnums[-1] + 1
        print(rnums)
        n = len(rnums)-1
        while n>=1:
            if rnums[n] == 10:
                rnums[n] = 0
                rnums[n-1] = rnums[n-1]+1
            n = n-1
        if rnums[0] == 0:
            rnums.pop(0)
        return rnums
# @lc code=end

print(Solution.plusOne(1,[9]))