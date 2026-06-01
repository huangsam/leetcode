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
        lo = 0
        hi = x
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            mid_sq = mid * mid

            if mid_sq == x:
                return mid
            elif mid_sq < x:
                lo = mid + 1
            else:
                hi = mid - 1

        return hi
