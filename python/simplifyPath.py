# https://leetcode.com/problems/simplify-path/

from typing import List


class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Assume that no spaces exist in folder names and file names.
        Then we can replace '/' with ' ' - so that 1 or more spaces
        can be split conveniently. Then for all the incoming tokens
        that are parsed, we check if it's a '.', '..' or something
        else. '.' is a no-op as it points to the current directory.
        A '..' is the previous directory, so we pop out the current
        directory. Everything else is a new name.
        """
        path_stack: List[str] = []

        for token in path.replace("/", " ").split():
            if token == '.':
                continue
            elif token == '..':
                if len(path_stack) > 0:
                    _ = path_stack.pop()
            else:
                path_stack.append(token)

        return "/" + "/".join(path_stack)
