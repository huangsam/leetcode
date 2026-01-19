# https://leetcode.com/problems/string-compression/

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Compress a list of characters in-place using run-length encoding.

        For each group of consecutive identical characters, replace the group
        with the character followed by the count of characters in that group.
        If the count is 1, do not append the count.

        Complexity:
        - Time: O(n), where n is the length of chars.
        - Space: O(1)
        """
        write_ptr = 0
        read_ptr = 0

        while read_ptr < len(chars):
            char = chars[read_ptr]
            count = 0

            # Find the length of the current group of identical characters
            while read_ptr < len(chars) and chars[read_ptr] == char:
                read_ptr += 1
                count += 1

            # Write the character
            chars[write_ptr] = char
            write_ptr += 1

            # Write the count if it's greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write_ptr] = digit
                    write_ptr += 1

        return write_ptr
