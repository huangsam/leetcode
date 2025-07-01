# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """
        Get binary representations of a, b, c and join them together.

        Iterate through them simultaneously, provided that they are the same length.

        For any output bit that does not match c, a and/or b should change.

        For any changes to a or b, they should be added to the tally of total swaps.
        """
        list_a = self._toList(a)
        list_b = self._toList(b)
        list_c = self._toList(c)

        min_swaps = 0

        # Iterate through the flags, bit by bit
        for bit_a, bit_b, bit_c in zip(list_a, list_b, list_c):
            if bit_a | bit_b == bit_c:  # Skip if the operation matches as expected
                continue
            if bit_a == bit_b == 1:  # Both bits must be flipped to go as expected
                min_swaps += 2
            else:  # Either bit can be flipped to go to False or True
                min_swaps += 1

        return min_swaps

    def _toList(self, num: int) -> list[bool]:
        # Note that 2^32 > 10^9 which is the limit of numbers possible
        return [i == "1" for i in format(num, "032b")]
