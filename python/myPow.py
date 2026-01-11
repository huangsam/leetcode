# https://leetcode.com/problems/powx-n/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Implement pow(x, n) to calculate x raised to the power n.

        We use exponentiation by squaring for efficiency. Handle negative n by
        taking reciprocal and making n positive. Then, while n > 0, if n is odd,
        multiply result by x, then square x and halve n.

        Complexity:
        - Time: O(log(n))
        - Space: O(1)
        """
        # Handle the case where n is 0
        if n == 0:
            return 1.00

        # Handle negative powers
        if n < 0:
            x = 1 / x
            n = abs(n)

        result = 1.00

        # Use exponentiation by squaring
        while n > 0:
            # If n is bitwise odd, multiply the result by x
            if n & 1:
                result *= x
            x *= x
            n >>= 1

        return result
