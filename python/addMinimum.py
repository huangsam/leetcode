# https://leetcode.com/problems/minimum-additions-to-make-valid-string/


class Solution:
    def addMinimum(self, word: str) -> int:
        """
        Find minimum additions to make a valid string. A string is valid
        if it can be formed by concatenating the string "abc" >= 1 times.

        Track the characters in the current "abc" sequence. If the next
        character is not greater than the last character, the current
        sequence cannot continue, so add the missing letters and reset
        the sequence. Finish by accounting for any final sequence.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        curr_seq: list[str] = []
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
