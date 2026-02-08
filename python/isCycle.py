# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional

from container.linked_list import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Determine if a linked list has a cycle.

        To solve this with O(1) memory, we use a slow pointer and a fast pointer.
        The slow pointer moves one step while the fast pointer moves two steps.

        Complexity:
        - Time: O(n)
        - Space: O(1)
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
