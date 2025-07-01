# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0
        while a > 0 or b > 0 or c > 0:
            a_bit = a & 1
            b_bit = b & 1
            c_bit = c & 1

            if a_bit | b_bit != c_bit:
                # Case 1: c_bit is 1, but (a_bit | b_bit) is not 1
                if c_bit == 1:
                    result += 1
                # Case 2: c_bit is 0, but (a_bit | b_bit) is not 0
                else:
                    result += 1 + (a_bit & b_bit)

            a >>= 1
            b >>= 1
            c >>= 1

        return result
