# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        root_node = prev_node = ListNode(-1)
        prev_node.next = head
        cur_node = head
        while cur_node is not None:
            if cur_node.val == val:
                prev_node.next = cur_node.next
            else:
                prev_node = cur_node
            cur_node = cur_node.next
        return root_node.next
