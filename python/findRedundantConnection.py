# https://leetcode.com/problems/redundant-connection/


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        """
        Find the edge to remove so that the graph is a tree. If there are
        multiple edges, return the one that appears last in input.

        Uses union-find to find the first edge where both nodes
        resolve to the same root.

        Complexity:
        - Time: O(e log v) with path compression
        - Space: O(v) for parent array and recursion stack
        """
        # We are guaranteed one additional edge
        n = len(edges)
        # Every node starts as its own root
        parent = list(range(n + 1))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> bool:
            root_a, root_b = find(a), find(b)
            if root_a == root_b:
                return False
            parent[root_b] = root_a
            return True

        for edge_a, edge_b in edges:
            if not union(edge_a, edge_b):
                return [edge_a, edge_b]

        # This should NOT happen with LC constraints
        return [-1, -1]
