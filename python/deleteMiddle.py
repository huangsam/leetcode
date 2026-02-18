# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

from typing import Optional

from container.linked_list import ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Deletes the middle node of a singly linked list.
        If the list has an even number of nodes, the second middle node is deleted.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        # Handle base case of 0 or 1 node
        if not head or not head.next:
            return None

        # We want 'slow' to stop at the node BEFORE the middle
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow.next is the middle node; skip it
        slow.next = slow.next.next

        return head
