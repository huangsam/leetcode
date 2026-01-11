# https://leetcode.com/problems/linked-list-in-binary-tree/

from typing import Optional

from container.binary_tree import TreeNode
from container.linked_list import ListNode


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        """
        Check if a linked list is a subpath in a binary tree.

        Traverse the binary tree, and for each node that matches the head of the
        linked list, perform a DFS to check if the list forms a downward path.

        The DFS checks if the current tree node matches the current list node,
        and recurses on left or right child with next list node.

        Complexity:
        - Time: O(n * m)
        - Space: O(h)
        """
        if not head:
            return True
        if not root:
            return False

        # Try matching from current node, or search in left/right subtrees
        return self._matches(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def _matches(self, list_node: Optional[ListNode], tree_node: Optional[TreeNode]) -> bool:
        """
        Check if linked list matches path starting from current tree node.
        """
        if not list_node:
            return True  # Reached end of list - full match
        if not tree_node:
            return False  # Reached end of tree path - no match

        # Values must match, and rest of list must match in left or right subtree
        if list_node.val != tree_node.val:
            return False

        return self._matches(list_node.next, tree_node.left) or self._matches(list_node.next, tree_node.right)
