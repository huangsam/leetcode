# https://leetcode.com/problems/add-binary/

from collections import deque
from typing import Deque


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(f"0b{a}", 2) + int(f"0b{b}", 2))[2:]

    def addBinaryManual(self, a: str, b: str) -> str:
        a_idx = len(a) - 1
        b_idx = len(b) - 1
        buffer: Deque[str] = deque()
        carry = 0

        while a_idx >= 0 or b_idx >= 0:
            a_val = int(a[a_idx]) if a_idx >= 0 else 0
            b_val = int(b[b_idx]) if b_idx >= 0 else 0

            ab_sum = a_val + b_val + carry
            carry = ab_sum >= 2

            if ab_sum % 2:
                buffer.appendleft("1")
            else:
                buffer.appendleft("0")

            # Move from right to left
            a_idx -= 1
            b_idx -= 1

        # Handle edge case here
        if carry:
            buffer.appendleft("1")

        # This should be the final result
        return "".join(buffer)
