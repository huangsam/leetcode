# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from collections import deque
from typing import Deque, List, Optional

from container.binary_tree import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build(deque(preorder), inorder)

    def build(self, prequeue: Deque[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None

        idx = inorder.index(prequeue.popleft())
        root = TreeNode(inorder[idx])

        root.left = self.build(prequeue, inorder[:idx])
        root.right = self.build(prequeue, inorder[idx + 1 :])

        return root
