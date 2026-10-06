# https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Find the length of the longest substring containing the same letter you
        can get after performing at most k character replacements.

        Approach:
        - Maintain a sliding window [left, right] and a character frequency map
        - Track max_freq as the highest count of any character seen in the window
        - Window is valid when (window_length - max_freq) <= k
        - When invalid, shrink from left and decrement count of s[left]
        - Track and return the maximum valid window length observed

        Complexity:
        - Time: O(n) where n is the length of string s
        - Space: O(1) auxiliary space (at most 26 uppercase English letters)
        """
        count: dict[str, int] = defaultdict(int)
        left = 0
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])

            # If replacements needed exceed k, shrink window
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
