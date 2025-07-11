# https://leetcode.com/problems/sort-list/

from typing import Optional

from container.linked_list import ListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        middle = self._getMiddle(head)
        right = middle.next
        middle.next = None
        l_sorted = self.sortList(head)
        r_sorted = self.sortList(right)
        return self._mergeSortedLists(l_sorted, r_sorted)

    def _getMiddle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def _mergeSortedLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        node.next = l1 or l2
        return dummy.next
