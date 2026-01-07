// https://leetcode.com/problems/number-of-islands/

public class NumberOfIslands {
    /**
     * Calculate number of islands by traversing the grid and
     * marking visited land cells.
     *
     * <p>Complexity:
     *
     * <ul>
     *     <li>Time: O(m * n)</li>
     *     <li>Space: O(m * n)</li>
     * </ul>
     */
    public int numIslands(char[][] grid) {
        int result = 0;
        boolean[][] visited = new boolean[rowCount(grid)][colCount(grid)];

        // Note that i stands for row, j stands for column
        for (int i = 0; i < rowCount(grid); i++) {
            for (int j = 0; j < colCount(grid); j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    traverseAndTrack(grid, i, j, visited);
                    result++;
                }
            }
        }

        return result;
    }

    private void traverseAndTrack(
            char[][] grid, int i, int j,
            boolean[][] visited) {
        // Out of bounds
        if (i < 0 || i >= rowCount(grid) || j < 0 || j >= colCount(grid)) {
            return;
        }

        // Visited or found water
        if (visited[i][j] || grid[i][j] == '0') {
            return;
        }

        // Mark as partially visited
        visited[i][j] = true;

        // Traverse in all 4 directions
        traverseAndTrack(grid, i + 1, j, visited); // down
        traverseAndTrack(grid, i - 1, j, visited); // up
        traverseAndTrack(grid, i, j + 1, visited); // right
        traverseAndTrack(grid, i, j - 1, visited); // left
    }

    private int rowCount(char[][] grid) {
        return grid.length;
    }

    private int colCount(char[][] grid) {
        return grid[0].length;
    }
}
