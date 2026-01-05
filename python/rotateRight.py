# https://leetcode.com/problems/rotate-list/

from typing import Optional

from container.linked_list import ListNode


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Time: O(n)
        Space: O(1)

        One possible approach is as follows:

        - Get length of list in one pass
        - Compute (k % length) and create a pointer at this distance
        - Set left node as head, set right node as head + distance
        - Iterate until next pointer of distance pointer is null (i.e. tail)
        - Unlink left.next from the target node
        - Link tail.next to the original head
        - Return the target node
        """
        if not head:
            return None

        curr, size = head, 0
        while curr:
            curr = curr.next
            size += 1

        window = k % size
        if window == 0:
            return head

        left, right = head, head
        for _ in range(window):
            right = right.next

        while right.next:
            left = left.next
            right = right.next

        # Collect target pointer and unlink left node from it
        target = left.next
        left.next = None

        # Link tail to original head
        right.next = head

        # Return target pointer
        return target
