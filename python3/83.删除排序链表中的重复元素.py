#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head:
            prenode = head
            while prenode.next is not None:
                node = prenode.next
                if node.val == prenode.val:
                    prenode.next = node.next
                else:
                    prenode = prenode.next
                if prenode is None:
                    break
            return head
        else:
            return head
# @lc code=end

