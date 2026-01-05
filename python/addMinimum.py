# https://leetcode.com/problems/minimum-additions-to-make-valid-string/

from typing import List


class Solution:
    def addMinimum(self, word: str) -> int:
        """
        Time: O(n)
        Space: O(n)

        a -> 2
        b -> 2
        c -> 2
        ab -> 1
        bc -> 1
        abc -> 0
        """
        curr_seq: List[str] = []
        num_letters = 0

        for ch in word:
            # If we find a character of earlier/same ascii value
            # then we tally our score and reset the sequence
            if len(curr_seq) > 0 and ch <= curr_seq[-1]:
                num_letters += 3 - len(curr_seq)
                curr_seq = []

            # Always add to the current sequence so that we
            # know how many characters are valid in the current
            # sequence
            curr_seq.append(ch)

        # It is possible that the last sequence is not cleared at the
        # end of the main loop, so we handle it here
        return num_letters + (3 - len(curr_seq))
