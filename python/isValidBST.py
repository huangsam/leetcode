# https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional

from model.binary_tree import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Check if the binary tree is a valid BST.

        We use an iterative in-order traversal to check if the values are in strictly
        increasing order.

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        st: list[TreeNode] = []
        curr = root
        prev = None

        while len(st) > 0 or curr:
            while curr:
                st.append(curr)
                curr = curr.left

            # Pop once to emulate an in-order visit
            curr = st.pop()

            if prev and prev.val >= curr.val:
                return False

            # Look at the right subtree of each node
            prev = curr
            curr = curr.right

        return True
