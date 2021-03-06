# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        result = self.inorderTraversal(root.left)
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))
        return result

    def inorderTraversalIterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        visited = []
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
