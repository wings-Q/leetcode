#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        depth = 0
        list = [root]
        while len(list)!=0:
            depth += 1
            for i in range(len(list)):
                if list[0].left:
                    list.append(list[0].left)
                if list[0].right:
                    list.append(list[0].right)
                del list[0]
        return depth

# @lc code=end

