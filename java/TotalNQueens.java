// https://leetcode.com/problems/n-queens-ii/

public class TotalNQueens {
    private int numberOfSolutions = 0;    /**
     * Time: O(n!)
     * Space: O(n)
     *
     * We know that 1 <= n <= 9, so time complexity isn't going to be
     * as big of a problem in this case. We just need to make sure
     * that we get the correct answer by backtracking solution. So
     * instead of saying that we got the right answer, we're saying
     * how many answers we got.
     */
    public int totalNQueens(int n) {
        helper(new int[n][n], 0);
        return numberOfSolutions;
    }

    /**
     * Proceed through columns until we reach the end, checking whether
     * any of the rows would be safe from a left-looking POV. When we
     * are at the end, we are guaranteed to have a solution, and we
     * add to the total counter.
     */
    private void helper(int[][] grid, int col) {
        if (col == grid.length) {
            numberOfSolutions++;
            return;
        }
        for (int row = 0; row < grid.length; row++) {
            if (isSafe(grid, row, col)) {
                grid[row][col] = 1;
                helper(grid, col + 1);
                grid[row][col] = 0;
            }
        }
    }

    private boolean isSafe(int[][] grid, int row, int col) {
        // Northwest
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (grid[i][j] == 1) {
                return false;
            }
        }

        // Southwest
        for (int i = row + 1, j = col - 1; i < grid.length && j >= 0; i++, j--) {
            if (grid[i][j] == 1) {
                return false;
            }
        }

        // West
        for (int i = col - 1; i >= 0; i--) {
            if (grid[row][i] == 1) {
                return false;
            }
        }

        return true;
    }
}
