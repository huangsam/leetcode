# https://leetcode.com/problems/rotting-oranges/


from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """
        Find the least amount of minutes for oranges to rot.

        Shortest-path -> BFS. We need multiple rounds of BFS so we check the
        queue length and the number of fresh oranges left.

        Complexity:
        - Time: O(m*n) where m = rows and n = cols
        - Space: O(m*n)
        """
        m, n = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        fresh_count = 0
        q: deque[tuple[int, int]] = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                elif grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        # Every iteration runs rotten bfs, prepares the q for next
        # iter and raises days by 1
        days_elapsed = 0
        while q and fresh_count > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for dir_i, dir_j in directions:
                    i_adj = i + dir_i
                    j_adj = j + dir_j
                    if 0 <= i_adj < m and 0 <= j_adj < n:
                        # Fresh -> rotten transition
                        if grid[i_adj][j_adj] == 1:
                            grid[i_adj][j_adj] = 2
                            fresh_count -= 1
                            q.append((i_adj, j_adj))
            days_elapsed += 1

        return days_elapsed if fresh_count == 0 else -1
