# https://leetcode.com/problems/sort-list/


from python.model.linked_list import ListNode


class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        """
        Sort a linked list in ascending order.

        We implement merge sort for linked lists. First, find the middle of the list
        using slow and fast pointers. Recursively sort the left and right halves,
        then merge the two sorted lists into one sorted list.

        Complexity:
        - Time: O(n * log(n))
        - Space: O(log(n))
        """
        if head is None or head.next is None:
            return head
        middle = self._getMiddle(head)
        right = middle.next
        middle.next = None
        l_sorted = self.sortList(head)
        r_sorted = self.sortList(right)
        return self._mergeSortedLists(l_sorted, r_sorted)

    def _getMiddle(self, head: ListNode) -> ListNode:
        """Find the middle of the linked list using slow and fast pointers."""
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def _mergeSortedLists(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        """Merge two sorted linked lists."""
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
