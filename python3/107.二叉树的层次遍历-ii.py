#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        list = [(0,root)]
        num = []
        while list:
            depth,node = list.pop()
            if len(num) > depth:
                num[depth].append(node.val)
            else:
                num.append([node.val])
            if node.right != None:
                list.append((depth+1,node.right))
            if node.left != None:
                list.append((depth+1,node.left))
        return num[::-1]
# @lc code=end

a = []
