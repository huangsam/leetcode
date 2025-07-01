# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # Calculate longest length
        longest = 0
        a_tmp, b_tmp, c_tmp = a, b, c
        while a_tmp | b_tmp | c_tmp:
            a_tmp = a_tmp >> 1
            b_tmp = b_tmp >> 1
            c_tmp = c_tmp >> 1
            longest += 1

        # Calculate the number of moves from [0, longest)
        result = 0
        for shift in range(longest):
            a_one = (a >> shift) & 1
            b_one = (b >> shift) & 1
            c_one = (c >> shift) & 1
            if a_one | b_one == c_one:
                continue
            if c_one == 1:
                result += 1
            else:
                result += 1 + (a_one & b_one)

        return result
