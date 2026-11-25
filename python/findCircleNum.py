# https://leetcode.com/problems/number-of-provinces/


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        """
        Find the number of provinces with cities given an adjacency
        matrix where [i][i] == 1 and [i][j] == 1 only if city i
        is directly connected to j.

        We use DFS for this particular solution, noting that the graph
        is undirected and that post-processing is not needed.

        Complexity:
        - Time: O(n^2)
        - Space: O(n)
        """
        # Single set for undirected graph
        visited: set[int] = set()

        n = len(isConnected)
        count = 0

        def dfs(city: int) -> None:
            # Traversal visits city immediately
            visited.add(city)

            for j in range(n):
                if isConnected[city][j] == 1:
                    if j not in visited:
                        dfs(j)

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count
