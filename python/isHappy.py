# https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        seen_numbers = set()
        current = n
        while current != 1:
            current = self._getSquareSum(current)
            if current in seen_numbers:
                return False
            seen_numbers.add(current)
        return True

    def _getSquareSum(self, n: int) -> int:
        digits = [int(d) ** 2 for d in str(n)]
        return sum(digits)
