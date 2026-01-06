# https://leetcode.com/problems/simplify-path/

from typing import List


class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Simplify a Unix-style file path.

        Complexity:
        - Time: O(n)
        - Space: O(n)

        Assume that no spaces exist in folder names and file names.
        Then we can split by '/' to identify all incoming tokens.
        For each token, we check if it's a '.', '..' or something
        else. '.' is a no-op as it points to the current directory.
        A '..' is the previous directory, so we pop it out.
        Everything else is a new name so we add it.
        """
        path_stack: List[str] = []

        for token in path.split("/"):
            if token in {"", "."}:
                continue
            elif token == "..":
                if len(path_stack) > 0:
                    _ = path_stack.pop()
            else:
                path_stack.append(token)

        return "/" + "/".join(path_stack)
