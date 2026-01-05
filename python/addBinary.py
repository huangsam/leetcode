# https://leetcode.com/problems/add-binary/

from collections import deque
from typing import Deque


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Time: O(n + m)
        Space: O(1)
        """
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinaryManual(self, a: str, b: str) -> str:
        """
        Time: O(max(n, m))
        Space: O(max(n, m))
        """
        a_idx, b_idx = len(a) - 1, len(b) - 1
        carry = 0
        buffer: Deque[str] = deque()
        while a_idx >= 0 or b_idx >= 0 or carry:
            a_val = int(a[a_idx]) if a_idx >= 0 else 0
            b_val = int(b[b_idx]) if b_idx >= 0 else 0

            # Sum of val and carry goes up to 3, so divmod works here
            carry, digit = divmod(a_val + b_val + carry, 2)

            # Append digits from right to left
            buffer.appendleft(str(digit))

            a_idx -= 1
            b_idx -= 1
        return "".join(buffer)
