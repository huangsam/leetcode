# https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import Optional

from container.random_linked_list import Node


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        Create a deep copy of a linked list with random pointers.

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        if not head:
            return None

        # Single mapping: old_node -> new_node
        old_to_new = {}

        # First pass: Create all new nodes
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: Connect next and random pointers
        curr = head
        while curr:
            new_node = old_to_new[curr]
            new_node.next = old_to_new.get(curr.next)
            new_node.random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new[head]
