# https://leetcode.com/problems/clone-graph/


class Node:
    def __init__(self, val: int = 0, neighbors: list["Node"] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        """
        Return a deep copy (clone) of the graph.

        We use a hash map instead of a hash set to store the mapping
        from original nodes to their clones. This allows us to easily
        retrieve the clone of a node when we encounter it again during
        the DFS traversal.

        Complexity:
        - Time: O(n + m), where n is node count and m is edge count
        - Space: O(n), for the visited dictionary and recursion stack
        """
        if not node:
            return None

        visited: dict[Node, Node] = {}

        def dfs(original_node: Node) -> Node:
            # 1. Check Map
            if original_node in visited:
                return visited[original_node]

            # 2. Create Shell
            clone = Node(original_node.val, [])

            # 3. Register
            visited[original_node] = clone

            # 4. Link Neighbors
            for neighbor in original_node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
