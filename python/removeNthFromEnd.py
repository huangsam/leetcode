# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from container.linked_list import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node_list = []
        curr_node = head
        while curr_node is not None:
            node_list.append(curr_node)
            curr_node = curr_node.next
        nlen = len(node_list)
        node_to_delete = node_list[nlen - n]
        if nlen - n > 0:
            prev_node = node_list[nlen - n - 1]
            prev_node.next = node_to_delete.next  # Bypass the node
        else:
            head = node_to_delete.next  # Remove head
        node_to_delete.next = None  # Clean up removed node
        return head
