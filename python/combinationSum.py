# https://leetcode.com/problems/combination-sum/


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Find all unique combinations in candidates where the candidate numbers sum to target.
        Any number in the combination may be used multiple times.

        Sorting the candidates allows for early termination. Note that in this case,
        number reuse implies that backtracking continues from the current index rather
        than moving to the next one.

        Complexity:
        - Time: O(n^t) where n is # of candidates and t is target value
        - Space: O(t)
        """
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
