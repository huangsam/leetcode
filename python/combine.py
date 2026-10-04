# https://leetcode.com/problems/combinations/


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        """
        Generate all possible combinations of k numbers chosen from the range 1 to n.

        We use a backtracking approach to generate all combinations. At each step,
        include the current number in the combination or skip it, and recursively
        generate the rest of the combination.

        Complexity:
        - Time: O(C(n, k) * k) where C(n, k) is the binomial coefficient
        - Space: O(k) for the recursion stack and path list
        """
        res: list[list[int]] = []
        path: list[int] = []

        def backtrack(start: int) -> None:
            # Add generated item once we have k items
            if len(path) == k:
                res.append(path.copy())
                return

            # Until base case, keep generating items
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)
        return res
