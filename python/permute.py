# https://leetcode.com/problems/permutations/


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        Return all possible permutations of an array of distinct integers.

        We use a backtracking approach to generate all permutations. At each step,
        we pick an available number, add it to the current path, and recursively
        generate the rest of the permutation.

        Complexity:
        - Time: O(n! * n)
        - Space: O(n)
        """
        res: list[list[int]] = []
        path: list[int] = []
        n = len(nums)

        def backtrack(mask: int) -> None:
            # Base case: we have collected all numbers in the path
            if len(path) == n:
                res.append(path.copy())
                return

            # Recursive case: pick an available number and continue
            for i, num in enumerate(nums):
                if not mask & (1 << i):
                    path.append(num)
                    backtrack(mask | (1 << i))
                    path.pop()

        backtrack(0)
        return res
