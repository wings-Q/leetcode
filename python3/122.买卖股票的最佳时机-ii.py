#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        gets=[0]
        if prices:
            price1 = prices[0]
            get = 0
            maxget = get
            for price2 in prices[1::]:
                if price2-price1>=0:
                    get = get+price2-price1
                if get > maxget:
                    maxget = get
                price1 = price2
            return maxget
        else:
            return 0
# @lc code=end

