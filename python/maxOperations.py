# https://leetcode.com/problems/max-number-of-k-sum-pairs/

from collections import Counter
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Find the maximum number of k-sum pairs in the list.

        Use a frequency map to count occurrences of each number.
        Then iterate through the unique numbers to find pairs that sum to k.

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        freq = Counter(nums)
        result = 0

        for a in freq:
            b = k - a

            # If the complement doesn't exist, skip
            if b not in freq:
                continue

            # To avoid double counting, only count pairs where a <= b
            if a < b:
                result += min(freq[a], freq[b])
            elif a == b:
                result += freq[a] // 2

        return result
