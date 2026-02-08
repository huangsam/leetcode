# https://leetcode.com/problems/decode-string/


class Solution:
    def decodeString(self, s: str) -> str:
        """
        Decode the given encoded string. The encoded string is in the format
        k[encoded_string], where the encoded_string inside the square brackets
        is repeated exactly k times.

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        stack = []
        current_str = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                # Building the multiplier (handles multi-digits like '100')
                current_num = current_num * 10 + int(char)

            elif char == "[":
                # We hit a bracket: Save the context
                # Push the current string and the multiplier onto the stack
                stack.append((current_str, current_num))
                # Reset for the new inner content
                current_str = ""
                current_num = 0

            elif char == "]":
                # End of a block: Pop the last saved context
                last_str, num = stack.pop()
                # The new current_str is:
                # The string before the bracket + (multiplier * inner string)
                current_str = last_str + (num * current_str)

            else:
                # Just a normal letter: Add it to our current working string
                current_str += char

        return current_str
