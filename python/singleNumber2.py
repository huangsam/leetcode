# https://leetcode.com/problems/single-number-ii/

from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Find the element that appears only once when others appear three times.

        Since all elements except one appear exactly three times, we can use a
        frequency map to count occurrences of each number. The element with a
        count of 1 is the one that appears only once.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        num_to_freq: DefaultDict[int, int] = defaultdict(int)
        for num in nums:
            num_to_freq[num] += 1
        for num, freq in num_to_freq.items():
            if freq == 1:
                return num
        raise ValueError("Input must have one item which appears once!")
