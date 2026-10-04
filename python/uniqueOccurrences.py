# https://leetcode.com/problems/unique-number-of-occurrences/

from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        """
        Given an array of integers arr, return true if the number of occurrences
        of each value in the array is unique, or false otherwise.

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        num_freq: Counter = Counter(arr)
        freq_seen: set[int] = set()
        for freq in num_freq.values():
            if freq in freq_seen:
                return False
            freq_seen.add(freq)
        return True
