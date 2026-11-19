# https://leetcode.com/problems/permutation-in-string/


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Check if s2 contains a permutation of s1.

        In this context, a permutation is really just an anagram. This
        insight guides us to use a 26-char ledger to track frequencies.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        if len(s1) > len(s2):
            return False

        k = len(s1)
        ledger = [0] * 26

        def index(ch: str) -> int:
            return ord(ch) - ord("a")

        for ch in s1:
            ledger[index(ch)] += 1

        for i in range(k):
            ledger[index(s2[i])] -= 1

        for right in range(k, len(s2)):
            left = right - k
            if all(i == 0 for i in ledger):
                return True
            ledger[index(s2[left])] += 1
            ledger[index(s2[right])] -= 1

        return all(i == 0 for i in ledger)
