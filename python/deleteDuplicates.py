# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

from collections import defaultdict
from typing import DefaultDict, Optional

from container.linked_list import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Remove duplicates from a sorted linked list, keeping only unique elements.
        
        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        val_freq: DefaultDict[int, int] = defaultdict(int)
        all_nodes = []

        curr = head
        while curr:
            val_freq[curr.val] += 1
            all_nodes.append(curr)
            curr = curr.next

        # Add dummy to handle 1 node and 2..n node cases
        dummy = prev = ListNode(next=None)

        curr = head
        while curr:
            temp = curr.next
            if val_freq.get(curr.val) == 1:
                prev.next = curr
                prev = curr
                curr.next = None
            curr = temp

        return dummy.next
