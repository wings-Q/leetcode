#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prestr = strs[0]
        for str in strs:
            for i in len(str):
                print(str[i:i+1])
                if str[i:i+1] != prestr[i:i+1]:
                    prestr = prestr[:i]
                    break

        return prestr
# @lc code=end

print(Solution.longestCommonPrefix(["flower","flow","flight"]))