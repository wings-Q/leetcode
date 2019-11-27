#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        sumnum = 0
        '''
        if s == 'IV':
            return 4
        if s == 'IX':
            return 9
        if s == 'XL':
            return 40
        if s == 'XC':
            return 90
        if s == 'CD':
            return 400
        if s == 'CM':
            return 900
        '''
        preroman = ''
        for i in s:
            if i == 'I':
                num = 1
            if i == 'V':
                if preroman == 'I':
                    num = 3
                else:
                    num = 5
            if i == 'X':
                if preroman == 'I':
                    num = 8
                else:
                    num = 10
            if i == 'L':
                if preroman == 'X':
                    num = 30
                else:
                    num = 50
            if i == 'C':
                if preroman == 'X':
                    num = 80
                else:
                    num = 100
            if i == 'D':
                if preroman == 'C':
                    num = 300
                else:
                    num = 500
            if i == 'M':
                if preroman == 'C':
                    num = 800
                else:
                    num = 1000
            sumnum = sumnum + num
            preroman = i
        return sumnum
        
# @lc code=end

