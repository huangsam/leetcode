# https://leetcode.com/problems/remove-linked-list-elements/

from container.linked_list import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
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
