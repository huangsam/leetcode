# https://leetcode.com/problems/equal-row-and-column-pairs/

from collections import defaultdict
from typing import DefaultDict, List, Tuple


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
        Count the number of pairs of rows and columns that are equal.

        We can do this by hashing each row and column into a tuple and counting
        the occurrences of each hash. Then, for each unique row hash, we can
        multiply the count of that row hash by the count of the corresponding
        column hash to get the number of pairs for that hash.

        Complexity:
        - Time: O(n^2) to hash all rows and columns
        - Space: O(k) where k is the number of unique row/column hashes
        """
        pair_count = 0

        row_map: DefaultDict[Tuple[int, ...], int] = defaultdict(int)
        col_map: DefaultDict[Tuple[int, ...], int] = defaultdict(int)

        # Get the number of row tuple occurences
        for row in grid:
            row_map[tuple(row)] += 1

        # Get the number of column tuple occurences
        for col in zip(*grid):
            col_map[col] += 1

        # Sum the combinations for each matching tuple
        for row_hash in row_map:
            pair_count += row_map[row_hash] * col_map[row_hash]

        return pair_count
