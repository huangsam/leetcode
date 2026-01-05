# https://leetcode.com/problems/generate-parentheses/

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Time: O(4^n / sqrt(n))
        Space: O(4^n / sqrt(n))
        """
        result: List[str] = []
        self._backtrack("", 0, 0, n, result)
        return result

    def _backtrack(self, current_string: str, open_count: int, close_count: int, n: int, result_list: List[str]):
        # Base Case: We've formed a complete, valid parenthesis string
        if open_count == close_count == n:
            result_list.append(current_string)
            return

        # Recursive Step 1: Add an opening parenthesis if allowed
        # We start with '(' as that must be the opening piece of any valid string
        # Getting out of this loop implies that we "remove" a character from here
        if open_count < n:
            self._backtrack(current_string + "(", open_count + 1, close_count, n, result_list)

        # Recursive Step 2: Add a closing parenthesis if allowed
        # We end with ')' as that must be the closing piece of any valid string
        if close_count < open_count:
            self._backtrack(current_string + ")", open_count, close_count + 1, n, result_list)
