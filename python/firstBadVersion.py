# https://leetcode.com/problems/first-bad-version/

# Example of a possible answer (>=1)
ANSWER = 4


def isBadVersion(version: int) -> bool:
    """Assume that this function is provided."""
    return version >= ANSWER


class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        lo_bad = isBadVersion(lo)
        if lo_bad:
            return lo
        hi = n
        hi_bad = isBadVersion(hi)
        result = -1
        while lo < hi:
            mid = (lo + hi) // 2
            mid_bad = isBadVersion(mid)
            if lo_bad:
                # Look between (lo, mid)
                result = lo
                hi = mid
                hi_bad = isBadVersion(hi)
            elif mid_bad:
                # Look between (lo + 1, mid)
                result = mid
                lo, hi = lo + 1, mid
                lo_bad = isBadVersion(lo)
                hi_bad = isBadVersion(hi)
            elif hi_bad:
                # Look between (mid + 1, hi)
                result = hi
                lo = mid + 1
                lo_bad = isBadVersion(lo)
        return result
