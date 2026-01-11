# https://leetcode.com/problems/sqrtx/


class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Calculate the square root of x rounded down to nearest integer.

        Use binary search: set lo=0, hi=x. While lo < hi, mid = (lo+hi)/2.

        If mid*mid > x, hi = mid. Else lo = mid+1 (for integer).

        Return lo-1.

        Complexity:
        - Time: O(log(x))
        - Space: O(1)
        """
        lo: int | float = 0
        hi: int | float = x
        while lo < hi:
            mid = (lo + hi) / 2
            mid_sq = mid * mid

            # Answer is close enough
            if abs(x - mid_sq) < 0.0001:
                floor, ceil = int(mid), int(mid) + 1
                if ceil * ceil == x:
                    return ceil
                else:
                    return floor

            # Arrange lo, hi for overshoot
            if mid_sq > x:
                hi = mid

            # Arrange lo, hi for undershoot
            elif mid_sq < x:
                lo = mid

        # Handle case when x is 0
        return 0
