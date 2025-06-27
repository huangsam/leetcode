# https://leetcode.com/problems/power-of-four/


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return True

        # Fill in powers of four in binary up to 32 bits
        binary_mask = "0b" + "00101010101010101010101010101010"[::-1]

        # Check if num is a power of two and if it matches the binary mask for powers of four
        return (num & (num - 1)) == 0 and (num & int(binary_mask, 2)) == num
