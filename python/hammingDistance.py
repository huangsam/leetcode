# https://leetcode.com/problems/hamming-distance/


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """Calculate the Hamming distance between two integers.
        
        The Hamming distance is the number of positions at which the corresponding bits are different.
        Uses XOR to identify differing bits, then counts the number of 1s in the result.
        """
        distance = 0
        # XOR gives 1 where bits differ, 0 where they're the same
        xor_result = x ^ y

        # Count the number of 1s in the XOR result
        while xor_result > 0:
            xor_result, remainder = divmod(xor_result, 2)
            distance += remainder

        return distance
