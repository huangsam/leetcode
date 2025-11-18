# https://leetcode.com/problems/merge-two-binary-trees/

from container.binary_tree import TreeNode


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """Merge two binary trees by summing overlapping node values.
        
        If nodes from both trees exist at the same position, their values are summed.
        If only one node exists, it's used directly.
        """
        # If one tree is None, return the other tree
        if t1 is None:
            return t2
        elif t2 is None:
            return t1
        # Create new node with sum of both values
        node = TreeNode(t1.val + t2.val)
        # Recursively merge left and right subtrees
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)
        return node
