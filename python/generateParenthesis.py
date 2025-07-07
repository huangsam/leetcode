from collections import deque
from typing import Deque, List


# TODO: Implement backtracking solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result: List[str] = []

        # To process all possible combinations
        boundary = 2 ** (n * 2)
        for i in range(1, boundary):
            pattern = self._buildPattern(i)
            if self._isValidPattern(pattern, n * 2):
                result.append(pattern)

        return result

    def _buildPattern(self, i: int) -> str:
        sequence: Deque[str] = deque()
        while i > 0:
            ch = "(" if i & 1 else ")"
            sequence.appendleft(ch)
            i >>= 1
        return "".join(sequence)

    def _isValidPattern(self, pattern: str, size: int) -> bool:
        if len(pattern) != size:
            return False

        st: List[str] = []
        for val in pattern:
            if val == "(":
                st.append(val)
            elif len(st) == 0:
                return False
            else:
                st.pop()

        return len(st) == 0
