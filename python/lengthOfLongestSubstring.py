class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_set = set()
        left = 0

        # Iterate through the string
        for right in range(len(s)):

            # We have a new unique character
            if s[right] not in char_set:
                char_set.add(s[right])
                max_length = max(max_length, right - left + 1)

            # We have an old character that came up again
            else:
                while s[right] in char_set:
                    char_set.remove(s[left])
                    left += 1
                char_set.add(s[right])
        
        return max_length
