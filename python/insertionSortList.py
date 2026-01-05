# https://leetcode.com/problems/insertion-sort-list/

from container.linked_list import ListNode


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        """
        Complexity:
        - Time: O(n^2)
        - Space: O(1)
        """
        p = dummy = ListNode(0)  # Dummy head for the sorted list
        cur = dummy.next = head
        while cur and cur.next:
            val = cur.next.val
            if cur.val < val:
                cur = cur.next  # Already in order
                continue
            if p.next.val > val:
                p = dummy  # Reset pointer
            while p.next.val < val:
                p = p.next  # Find insertion point
            new = cur.next
            cur.next = new.next  # Remove from original list
            new.next = p.next  # Insert into sorted list
            p.next = new
        return dummy.next
