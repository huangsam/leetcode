# https://leetcode.com/problems/find-all-duplicates-in-an-array/
from typing import List


class Solution(object):
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        result = []
        for i in nums:
            if d.get(i, False):
                result.append(i)
            else:
                d[i] = True
        return result
