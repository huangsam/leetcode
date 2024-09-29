# https://leetcode.com/problems/jewels-and-stones/
class Solution(object):
    def numJewelsInStones(self, J: str, S: str) -> int:
        j_tally = {}
        for ch in J:
            j_tally[ch] = 0
        for ch in S:
            if ch in j_tally:
                j_tally[ch] += 1
        total = 0
        for _, val in j_tally.items():
            total += val
        return total
