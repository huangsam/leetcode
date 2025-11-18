# https://leetcode.com/problems/remove-linked-list-elements/

from container.linked_list import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """Remove all nodes from a linked list that have the specified value.
        
        Uses a dummy node to simplify handling of edge cases like removing the head node.
        """
        # Create dummy node to handle edge cases
        root_node = prev_node = ListNode(-1)
        prev_node.next = head
        cur_node = head
        while cur_node is not None:
            # If current node matches the value to remove, skip it
            if cur_node.val == val:
                prev_node.next = cur_node.next
            else:
                # Otherwise, move prev_node forward
                prev_node = cur_node
            cur_node = cur_node.next
        return root_node.next
