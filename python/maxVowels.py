# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        Return the maximum number of vowels in any substring of s with length k.

        Use a sliding window of size k to keep track of the number of vowels
        in the current window. Update the maximum count as we slide the window
        across the string.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        cur_vowels = 0
        vowels = {"a", "e", "i", "o", "u"}

        # Take care of initial 0:k
        for i in range(k):
            if s[i] in vowels:
                cur_vowels += 1

        # Take care of head and tail from here
        max_vowels = cur_vowels
        for i in range(k, len(s)):
            if max_vowels == k:
                return k

            # The new char that we're getting
            curr_ch = s[i]

            # The old char that we're discarding
            last_ch = s[i - k]

            if curr_ch in vowels:
                cur_vowels += 1
            if last_ch in vowels:
                cur_vowels -= 1

            # Get the best of the best
            max_vowels = max(max_vowels, cur_vowels)

        return max_vowels
