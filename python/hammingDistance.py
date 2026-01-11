# https://leetcode.com/problems/hamming-distance/


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        Calculate the Hamming distance between two integers.

        XOR the two numbers to identify bits that differ. Then count the number
        of 1s in the XOR result.

        Use a loop to divide by 2 and add the remainder each time until the number is 0.

        Complexity:
        - Time: O(log(max(x, y)))
        - Space: O(1)
        """
        distance = 0
        xor_result = x ^ y  # XOR will have 1s where bits differ
        while xor_result > 0:
            xor_result, remainder = divmod(xor_result, 2)  # Get the least significant bit
            distance += remainder  # Add 1 if the bit was set
        return distance
