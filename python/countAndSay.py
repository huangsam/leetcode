# https://leetcode.com/problems/count-and-say/

from typing import List


class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Generate the nth term of the count-and-say sequence.

        Start with '1'. For each subsequent term, iterate through the current string, counting consecutive identical digits.

        For each group, append the count followed by the digit to build the next term.

        Complexity:
        - Time: O(n * m)
        - Space: O(m)
        """
        if n == 1:
            return "1"

        # Start with the base case for n=1
        current_seq_str = "1"

        # Iterate from the 2nd sequence up to the nth sequence
        for _ in range(2, n + 1):
            next_seq_list: List[str] = []

            count = 1
            # Iterate through the characters of the current sequence string
            for j in range(len(current_seq_str)):
                # If it's not the last character and the current character
                # is the same as the next
                if j + 1 < len(current_seq_str) and current_seq_str[j] == current_seq_str[j + 1]:
                    count += 1
                else:
                    # If the character changes or it's the last character,
                    # append the count and the character to the next sequence
                    next_seq_list.append(str(count))
                    next_seq_list.append(current_seq_str[j])
                    count = 1  # Reset count for the new character sequence

            # Update current_seq_str for the next iteration
            current_seq_str = "".join(next_seq_list)

        return current_seq_str
