#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices):
        pricelist=[]
        gets=[0]
        if prices:
            price1 = prices[0]
            get = 0
            maxget = get
            for price2 in prices[1::]:
                if get+price2-price1>=0:
                    get = get+price2-price1
                else:
                    get = 0
                if get > maxget:
                    maxget = get
                price1 = price2
            return maxget
        else:
            return 0

# @lc code=end

Solution.maxProfit(1,[7,1,5,3,6,4])