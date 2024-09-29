# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional

from container.linked_list import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        To check cycle, we can use O(n) memory to store all
        seen nodes and report when the next one matches any
        of the seen ones. To do this with O(1) memory, we need
        to have a slow pointer and a fast pointer to loop around.
        If the fast pointer breaks, then the fast pointer
        can never catch up to the slow pointer. But if the
        fast pointer matches, then we know for sure that there
        is a cycle.
        """
        slow, fast = head, head
        while slow and fast:
            try:
                slow = slow.next
                fast = fast.next.next
            except AttributeError:
                break
            if id(slow) == id(fast):
                return True
        return False
