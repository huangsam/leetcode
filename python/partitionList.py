# https://leetcode.com/problems/partition-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        One approach:

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
            if curr.val < x:
                lt_tail.next = curr
                lt_tail = curr
            else:
                ge_tail.next = curr
                ge_tail = curr
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
