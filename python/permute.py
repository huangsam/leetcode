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
        used = [False] * len(nums)

        def backtrack() -> None:
            # Base case: no available numbers left
            if all(used):
                res.append(path.copy())
                return

            # Recursive case: pick an available number and continue
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(num)
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return res
