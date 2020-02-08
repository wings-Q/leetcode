#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        depths=[]
        list=[]
        if root:
            list.append((1,root))
            while list:
                depth,node = list.pop()
                if node.left is not None:
                    list.append((depth+1,node.left))
                if node.right is not None:
                    list.append((depth+1,node.right))
                if node.right is None and node.left is None:
                    depths.append(depth)
            return min(depths)        
        else:
            return 0
# @lc code=end


