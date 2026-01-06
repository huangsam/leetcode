# https://leetcode.com/problems/remove-linked-list-elements/

from container.linked_list import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        Remove all nodes with a specific value from a linked list.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        root_node = prev_node = ListNode(-1)  # Dummy node to handle head removal
        prev_node.next = head
        cur_node = head
        while cur_node is not None:
            if cur_node.val == val:
                prev_node.next = cur_node.next  # Skip the node
            else:
                prev_node = cur_node  # Move prev forward
            cur_node = cur_node.next  # Move current forward
        return root_node.next
