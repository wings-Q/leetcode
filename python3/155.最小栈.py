#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []

    def push(self, x: int) -> None:
        if self.list:
            minnumber = self.getMin()
            if x < minnumber:
                minnum = x
            else:
                minnum = minnumber
        else:
            minnum = x
        self.list.append((x,minnum))
    def pop(self) -> None:
        self.list.pop(-1)


    def top(self) -> int:
        x,minnum = self.list[-1]
        return x

    def getMin(self) -> int:
        x,minnum = self.list[-1]
        return minnum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

