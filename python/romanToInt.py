# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert a Roman numeral to an integer.

        Starting from left to right...

        When the symbol I is detected, followed by more Is, we are
        reaching a terminal endpoint.

        When any symbol is followed by a greater symbol, we subtract
        the value of the greater symbol by the smaller symbol.

        If a symbol is repeated, we multiply the frequency and then add
        it to the total.

        Otherwise, we continue to add the value of the current symbol
        to the total sum that we want.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return mapping[s[0]]

        # Start with first character
        curr_seq = [s[0]]

        # Keep a tally of the total
        total = 0

        # Go from left to right, starting from second character
        for ch in s[1:]:
            if curr_seq:
                prev_val = mapping[curr_seq[-1]]
                curr_val = mapping[ch]

                # We consume the previous character AND the current
                # character. Therefore, we need to clear out the
                # current sequence AND skip populating it
                if prev_val < curr_val:
                    total += curr_val - prev_val
                    curr_seq = []
                    continue

                # Do nothing, just let curr_seq continue to expand
                if prev_val == curr_val:
                    pass

                # We are proceeding to a "lower" level, so then we can
                # multiply the previous value, followed by the current
                # sequence
                else:
                    total += prev_val * len(curr_seq)
                    curr_seq = []

            # Always continue to append
            curr_seq.append(ch)

        # There may be some leftover in curr_seq. To handle that, we assume
        # curr_seq has the same character repeated 1-N times
        if len(curr_seq) > 0:
            return total + (mapping[curr_seq[-1]] * len(curr_seq))

        return total
