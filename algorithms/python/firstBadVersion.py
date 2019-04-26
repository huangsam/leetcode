# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


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
