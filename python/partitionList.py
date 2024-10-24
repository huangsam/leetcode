# https://leetcode.com/problems/partition-list/

from typing import Optional

from container.linked_list import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Partition nodes < x and >= x, preserving the order of the nodes.

        One approach to achieving the constraints above is to:

        - Build partial 1 with things < x
        - Build partial 2 with things >= x
        - Each time a new node is built, unlink old next pointer
        - Track the head and tail of both partial lists
        - Link tail of partial 1 with head of partial 2
        - Return head of the partial 1
        """
        if not head:
            return None

        # Use dummy nodes to reduce null logic
        lt_head = ListNode()
        ge_head = ListNode()

        curr = head
        lt_tail = lt_head
        ge_tail = ge_head

        while curr:
            temp = curr.next

            # Add items to partial 1 with values < x
            if curr.val < x:
                lt_tail.next = curr
                lt_tail = curr

            # Add items to partial 2 with values >= x
            else:
                ge_tail.next = curr
                ge_tail = curr

            # Address next pointer on the tail node
            curr.next = None

            curr = temp

        # Partial 1 has some items to link to partial 2
        if lt_head is not lt_tail:
            lt_tail.next = ge_head.next

        # Partial 1 has no items to link to partial 2
        else:
            lt_head.next = ge_head.next

        # Access the dummy node to get the first node
        return lt_head.next
