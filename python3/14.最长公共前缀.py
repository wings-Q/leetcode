#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if strs == []:
            return ''
        prestr = strs[0]
        for str in strs:
            if str == '':
                return ''
            for i in range(len(str)):
                if str[i:i+1] != prestr[i:i+1]:
                    prestr = prestr[:i]
                    break
                if i == len(str)-1:
                    prestr = prestr[:i+1] 

        return prestr
# @lc code=end

print(Solution.longestCommonPrefix(1,["aa","a"]))