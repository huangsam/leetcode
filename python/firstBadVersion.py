# https://leetcode.com/problems/first-bad-version/

# Example of a possible answer (>=1)
ANSWER = 4


def isBadVersion(version: int) -> bool:
    """Assume that this function is provided."""
    return version >= ANSWER


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Time: O(log(n))
        Space: O(1)
        """
        lo, hi = 1, n
        while lo < hi:
            mid = lo + (hi - lo) // 2

            # Case 1: The first bad version could be right here or
            # it could be earlier
            if isBadVersion(mid):
                hi = mid
            # Case 2: The first bad version must be to the right of
            # this particular version, so let's go up
            else:
                lo = mid + 1

        # By this time, we have the first bad version since we have
        # effectively converged on a single point
        return lo
