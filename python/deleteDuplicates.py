# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
from collections import defaultdict


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val_freq: DefaultDict[Any, int] = defaultdict(int)
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
