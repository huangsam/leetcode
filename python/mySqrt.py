# https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        while lo < hi:
            mid = (lo + hi) / 2
            mid_sq = mid * mid

            # the answer is close enough
            if abs(x - mid_sq) < 0.0001:
                floor, ceil = int(mid), int(mid) + 1
                if ceil * ceil == x:
                    return ceil
                else:
                    return floor

            # arrange lo, hi for overshoot
            if mid_sq > x:
                lo, hi = lo, mid

            # arrange lo, hi for undershoot
            elif mid_sq < x:
                lo, hi = mid, hi

        # handles the case when x is 0
        return 0
