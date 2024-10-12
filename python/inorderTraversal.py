# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import List

from container.binary_tree import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = self.inorderTraversal(root.left)
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))
        return result

    def inorderTraversalIterative(self, root: TreeNode) -> List[int]:
        visited: List[int] = []
        c = root
        s = []
        while c is not None or len(s) > 0:
            while c is not None:
                s.append(c)
                c = c.left
            c = s.pop()
            visited.append(c.val)
            c = c.right
        return visited
