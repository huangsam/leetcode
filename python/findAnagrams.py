# https://leetcode.com/problems/find-all-anagrams-in-a-string/


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        """
        Return an array of all start indices of p's anagrams in s.

        We see that p is fixed length, so use a fixed length sliding
        window. As we iterate through, remove one char and add one
        char to the ledger.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        if len(p) > len(s):
            return []

        result: list[int] = []

        def index(ch: str) -> int:
            return ord(ch) - ord("a")

        # Tracks the counts as we go through sliding window
        ledger = [0] * 26
        for ch in p:
            ledger[index(ch)] += 1

        # Relying on a fixed length sliding window
        k = len(p)

        # Setup ledger properly prior to going further
        for i in range(k):
            ledger[index(s[i])] -= 1

        for right in range(k, len(s)):
            left = right - k
            if all(i == 0 for i in ledger):
                result.append(left)
            ledger[index(s[left])] += 1
            ledger[index(s[right])] -= 1

        # Addresses the last iteration
        if all(i == 0 for i in ledger):
            result.append(len(s) - k)

        return result
