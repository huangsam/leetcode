# https://leetcode.com/problems/linked-list-in-binary-tree/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        """
        Some observations so far:

        Subpath does not have to start from root. It can be at root, it
        can be in the middle of tree, or touch the bottom of the tree.
        All are valid.

        The typical preorder and inorder will not provide an easy
        solution. Postorder seems to be the most natural, since you
        get the result upwards at the top of the root node. Since we
        want to have a boolean outcome at the end of the day.
        """
        # Traverse head to get target_seq
        current = head
        target_seq = []
        while current:
            target_seq.append(current.val)
            current = current.next

        # Cross-check match count with target sequence size
        return len(target_seq) == self.matchWorker(root, target_seq)

    def matchWorker(self, root, target_seq) -> int:
        """Return number of matches relative to sequence.

        0 -> if 0 numbers match
        1 -> if 1 number matches
        2 -> if 2 numbers match in a row
        ...
        """
        # Null has 0 matches by default
        if root is None:
            return 0

        left_old = self.matchWorker(root.left, target_seq)
        right_old = self.matchWorker(root.right, target_seq)

        # Propogate answer if the sequence fully matched before
        if max(left_old, right_old) == len(target_seq):
            return len(target_seq)

        # The old answers act as an offset for target_seq
        left_index = len(target_seq) - left_old - 1
        right_index = len(target_seq) - right_old - 1

        left_new, right_new = 0, 0

        # See if left nodes match the sequence
        if left_index >= 0 and target_seq[left_index] == root.val:
            left_new = left_old + 1

        # See if right nodes match the sequence
        if right_index >= 0 and target_seq[right_index] == root.val:
            right_new = right_old + 1

        # Return the biggest answer, whether or not a match is found
        return max(left_new, right_new)
