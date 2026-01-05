# https://leetcode.com/problems/happy-number/

from typing import Set


class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Complexity:
        - Time: O(log(n))
        - Space: O(log(n))
        """
        seen_nums: Set[int] = set()
        current = n

        while current != 1:
            current = self._getSquareDigits(current)

            # Abort if an endless cycle is detected
            if current in seen_nums:
                return False

            seen_nums.add(current)

        # By this point, the value ends with 1
        return True

    def _getSquareDigits(self, val: int) -> int:
        result = 0

        # We are gauranteed that val >= 1
        while val > 0:
            # Add the square of each digit
            result += (val % 10) ** 2

            # Grab the next digit in store
            val //= 10

        return result
