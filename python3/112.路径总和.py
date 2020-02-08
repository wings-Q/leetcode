#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        sums=[]
        list=[]
        if root:
            list.append((root.val,root))
            while list:
                sumnum,node = list.pop()
                if node.left is not None:
                    list.append((sumnum+node.left.val,node.left))
                if node.right is not None:
                    list.append((sumnum+node.right.val,node.right))
                if node.right is None and node.left is None:
                    if sumnum is sum:
                        return True
                    sums.append(sumnum)
            return sum in sums      
        else:
            return False
# @lc code=end

