# https://leetcode.com/problems/combination-sum/


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res: list[list[int]] = []
        path: list[int] = []

        # Prepare candidates for quick break-out
        candidates.sort()

        def backtrack(start: int, remain: int) -> None:
            # Base case: remainder is now empty
            if remain == 0:
                res.append(path.copy())
                return

            # Recurring case: recurse onto itself *and* next items
            for i in range(start, len(candidates)):
                cand = candidates[i]
                if cand > remain:
                    break
                path.append(cand)
                backtrack(i, remain - cand)
                path.pop()

        backtrack(0, target)
        return res
