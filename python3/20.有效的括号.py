#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        slist = []
        leftdict = {'[':1,'{':2,'(':3}
        rightlist = {']':1,'}':2,')':3}
        for sym in s:
            if sym in leftdict:
                slist.append(leftdict[sym])
            elif sym in rightlist and slist != []:
                if rightlist[sym] == slist[-1]:
                    slist.pop()
                else:
                    return False
            else:
                return False
            #print(slist)
        if slist == []:
            return True
        else:
            return False

# @lc code=end
print(Solution.isValid(1,']'))
