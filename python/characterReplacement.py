# https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Find the length of the longest substring containing the same letter you
        can get after performing at most k character replacements.

        Approach:
        - Use a sliding window with two pointers (left, right) and a character
          frequency map.
        - Maintain `max_freq`, which tracks the count of the most frequent character
          within the current window.
        - A window is valid if: (window_length - max_freq) <= k, meaning the non-dominant
          characters can all be replaced with at most k operations.
        - If (right - left + 1) - max_freq > k, the window is invalid; shrink it from
          the left by decrementing the count of s[left] and advancing left.
          (Note: max_freq does not need to be decremented when shrinking because a
          smaller max_freq would only produce a shorter window, which cannot beat our best).
        - Track the maximum valid window size across the traversal.

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
