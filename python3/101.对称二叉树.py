#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        list = [(root,root)]
        while list:
            p,q = list.pop()
            if p == None and q == None:
                continue
            if p == None or q == None:
                return False
            if p.val == q.val:
                list.append((q.right,p.left))
                list.append((q.left,p.right))
            else:
                return False
        return True
# @lc code=end

