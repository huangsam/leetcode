# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

from typing import Optional

from model.linked_list import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Remove duplicates from a sorted linked list, keeping only unique elements.

        Use two pointers: prev tracks the last node to keep, curr traverses
        the list. Since the list is sorted, duplicates are consecutive. Skip
        entire groups of duplicates.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        dummy = ListNode(next=head)
        prev = dummy
        curr = head

        while curr:
            # Check if current value appears multiple times
            if curr.next and curr.val == curr.next.val:
                # Skip all nodes with the same value
                val = curr.val
                while curr and curr.val == val:
                    curr = curr.next
            else:
                # Single occurrence, keep this node
                prev.next = curr
                prev = curr
                curr = curr.next

        prev.next = None  # Prevent cycles
        return dummy.next
