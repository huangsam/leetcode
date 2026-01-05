# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time: O(n)
        Space: O(n)

        Check if parentheses are valid.

        Constraints:
        - Open brackets must be closed by the same type
        - Open brackets must be closed in the correct order
        - Close brackets has a corresponding open bracket

        Simplified: Stack alone is sufficient to validate.
        """
        stack = []
        close_to_open = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                # Must have matching open bracket on stack
                if not stack or stack[-1] != close_to_open[ch]:
                    return False
                stack.pop()

        # Valid if all brackets matched (stack empty)
        return len(stack) == 0
