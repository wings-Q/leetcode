#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        slist = s.split(" ")
        return len(slist[-1])
# @lc code=end

l = "a "
a = l[-1:]
print(a)