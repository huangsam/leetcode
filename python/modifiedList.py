# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Create hash set to avoid an expensive O(N) lookup on nums
        num_set = set(nums)

        # Initially, first and current should be the same thing
        first = current = head

        # Prev allows us to "delete" a node from the list
        prev = None

        while current is not None:
            next = current.next

            # Should be an O(1) check given that num_set is bounded
            # to 10^5
            if current.val in num_set:
                # Case 1: Current is the first node
                if first is current:
                    first = next

                # Case 2: Current is not the first node
                elif prev is not None:
                    prev.next = next

                # Current is cleared away and prev remains. So prev
                # pointer does not need to change at all
            else:
                # Current is not cleared so we change prev to point
                # at this node as we iterate through the OG list
                prev = current

            current = next

        # We ultimately want the head of the modified linked list
        return first
