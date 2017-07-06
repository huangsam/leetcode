# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node_list = []
        curr_node = head
        while curr_node is not None:
            node_list.append(curr_node)
            curr_node = curr_node.next
        node_to_delete = None
        nlen = len(node_list)
        node_to_delete = node_list[nlen - n]
        if nlen - n > 0:
            prev_node = node_list[nlen - n - 1]
            prev_node.next = node_to_delete.next
        else:
            head = node_to_delete.next
        node_to_delete.next = None
        return head
