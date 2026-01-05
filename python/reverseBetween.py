# https://leetcode.com/problems/reverse-linked-list-ii/

from typing import Optional

from container.linked_list import ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Complexity:
        - Time: O(n)
        - Space: O(1)

        We reverse a subset of the singly linked list from
        left <= right. Anything less than left and anything greater
        than right keeps the same ordering.

        The simplest way is to disconnect the left <= right subset
        from the linked list, reverse it and reconnect it back to
        the list afterward. Assuming that left > 1 or right still
        has at least one node afterward.

        Keep in mind that left can equal right. So in that case, nothing
        needs to be done as it were.
        """
        if not head:
            return None
        elif left == right:
            return head

        # Find point for breaking left (sentinel or real)
        break_left: ListNode = ListNode(val=-1000, next=head)
        for _ in range(left - 1):
            break_left = break_left.next

        # Find point for breaking right (null or real)
        break_right: ListNode | None = head
        for _ in range(right):
            if break_right:
                break_right = break_right.next

        # Reverse between left < right, since we know that
        # left != right by this point. By the end, we have
        # current pointing to the new head. Tail points to
        # the starting point
        current = break_left.next.next
        prev = break_left.next
        tail = prev
        for _ in range(right - left):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        # Reconnect broken left if applicable
        break_left.next = prev

        # Reconnect broken right if applicable
        tail.next = break_right

        return head if left > 1 else prev
