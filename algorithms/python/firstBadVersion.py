# https://leetcode.com/problems/first-bad-version/

# Example of a possible answer (>=1)
ANSWER = 4


def isBadVersion(version):
    """
    :type version: int
    :rtype: bool
    """
    return version >= ANSWER


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        l_bad = isBadVersion(l)
        if l_bad:
            return l
        h = n
        h_bad = isBadVersion(h)
        result = -1
        while l < h:
            m = (l + h) // 2
            m_bad = isBadVersion(m)
            if l_bad:
                # look between (l, m)
                result = l
                h = m
                h_bad = isBadVersion(h)
            elif m_bad:
                # look between (l + 1, m)
                result = m
                l, h = l + 1, m
                l_bad = isBadVersion(l)
                h_bad = isBadVersion(h)
            elif h_bad:
                # look between (m + 1, h)
                result = h
                l = m + 1
                l_bad = isBadVersion(l)
        return result
