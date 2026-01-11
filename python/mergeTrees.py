# https://leetcode.com/problems/merge-two-binary-trees/

from container.binary_tree import TreeNode


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        Merge two binary trees.

        Recursively traverse both trees: if one node is None, return the other.

        Otherwise, create a new node with value t1.val + t2.val, and set left to
        merge of lefts, right to merge of rights.

        Complexity:
        - Time: O(n)
        - Space: O(h)
        """
        if t1 is None:
            return t2
        elif t2 is None:
            return t1
        node = TreeNode(t1.val + t2.val)
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)
        return node
