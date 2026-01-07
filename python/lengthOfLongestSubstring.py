# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from typing import Set


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.

        Start by iterating through the entire string. We'll have a left
        and right pointer indicating a substring with the range
        [left, right]. If we encounter new characters, we increment right
        by one and update the maximum length as needed. If we encounter a
        duplicate, we increment left until that is no longer the case.

        Complexity:
        - Time: O(n)
        - Space: O(min(n, m))
        """
        max_length: int = 0
        char_seen: Set[str] = set()
        left: int = 0
        for right in range(len(s)):
            if s[right] not in char_seen:
                char_seen.add(s[right])
                max_length = max(max_length, right - left + 1)
            else:
                while s[right] in char_seen:
                    char_seen.remove(s[left])
                    left += 1
                char_seen.add(s[right])
        return max_length
