class Solution:
    def isValid(self, s: str) -> bool:
        """
        Constraints:
        - Open brackets must be closed by the same type
        - Open brackets must be closed in the correct order
        - Close brackets has a corresponding open bracket

        To satisfy constraint 1, we use a mapping
        To satisfy constraint 2, we use a stack
        To satisfy constraint 3, we check stack, match == close
        """
        open_st = []
        close_open = {')': '(', '}': '{', ']': '['}
        close_count, match_count = 0, 0
        for ch in s:
            if ch in '({[':
                open_st.append(ch)
            else:
                close_count += 1
                if open_st and open_st[-1] == close_open[ch]:
                    _ = open_st.pop()
                    match_count += 1
        return len(open_st) == 0 and close_count == match_count
