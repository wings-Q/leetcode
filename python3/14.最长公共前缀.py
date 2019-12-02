#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        '''
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
'''

        res = ""
        if len(strs) == 0:
            return ""
        for each in zip(*strs):#zip()函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
            if len(set(each)) == 1:#利用集合创建一个无序不重复元素集
                res += each[0]
            else:
                return res
        return res

# @lc code=end
'''test
print(Solution.longestCommonPrefix(1,["aa","a"]))
'''
'''
总结：对python中的list，tuple的操作函数：
set():创建无需不重复元素集合
zip():创建由tuple组成的list
'''