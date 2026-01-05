# https://leetcode.com/problems/jewels-and-stones/


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        """
        Time: O(n + m)
        Space: O(n)
        """
        j_tally = {}  # Dictionary to count jewels in stones
        for ch in J:
            j_tally[ch] = 0  # Initialize counts
        for ch in S:
            if ch in j_tally:
                j_tally[ch] += 1  # Increment if it's a jewel
        total = 0
        for _, val in j_tally.items():
            total += val  # Sum the counts
        return total
