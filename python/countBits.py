# https://leetcode.com/problems/counting-bits/
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Get the binary representation for each number i from
        0..n and literally count the number of 1s in each
        string.

        The alternative is to xor/and the powers of 2 to the
        each number i and tallying up the score. That would
        be a O(n lg n) algo in that case.
        """
        return [bin(i)[2:].count("1") for i in range(n + 1)]
