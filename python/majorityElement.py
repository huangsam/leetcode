# https://leetcode.com/problems/majority-element/
from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Given an array nums of size n, return the majority element.

        The majority element is the element that appears more than
        [n / 2] times. You may assume that the majority element always
        exists in the array.

        Approach 1:
        - Gather all counts by number
        - While doing so, report any number that occurs over [n/2]

        Follow-up: Could you solve the problem in linear time and in O(1) space?
        """
        counts_by_num: DefaultDict[int, int] = defaultdict(int)
        for num in nums:
            counts_by_num[num] += 1
            if counts_by_num[num] > len(nums) / 2:
                return num
        raise ValueError("Input list does not have a majority element")
