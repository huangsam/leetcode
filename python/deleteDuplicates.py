# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
from collections import defaultdict


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val_freq: Dict[Any, int] = defaultdict(int)
        all_nodes = []

        current = head
        while current:
            val_freq[current.val] += 1
            all_nodes.append(current)
            current = current.next

        # Add dummy to handle 1 node and 2..n node cases
        unique_nodes = [ListNode()]

        # Add nodes which do not have duplicates
        unique_nodes.extend(n for n in all_nodes if val_freq.get(n.val) == 1)

        # Abort processing if all nodes are duplicates of each other
        if len(unique_nodes) == 1:
            return None

        # We know that the linked list is already sorted, so
        # need to pre-sorting before linking things
        curr, prev = 1, 0
        while curr < len(unique_nodes):
            curr_node = unique_nodes[curr]
            prev_node = unique_nodes[prev]

            prev_node.next = curr_node
            prev_node = curr_node
            curr_node.next = None

            curr, prev = curr + 1, prev + 1

        # Return min node as it is unique, non-dupe, sorted
        return unique_nodes[1]
