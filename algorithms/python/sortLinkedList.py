# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        middle = self.getMiddle(head)
        right = middle.next
        middle.next = None
        l_sorted = self.sortList(head)
        r_sorted = self.sortList(right)
        return self.mergeSortedLists(l_sorted, r_sorted)

    def getMiddle(self, head):
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def mergeSortedLists(self, l1, l2):
        dummy = ListNode(None)
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
