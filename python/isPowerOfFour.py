# https://leetcode.com/problems/power-of-four/


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        """
        Determine if a number is a power of four.
        
        Complexity:
        - Time: O(1)
        - Space: O(1)
        """
        if num <= 0:
            return False

        # Fill in powers of four in binary up to 32 bits
        binary_mask = 0b01010101010101010101010101010101

        # Check if num is a power of two and if it matches the binary mask for powers of four
        return (num & (num - 1)) == 0 and (num & binary_mask) == num
