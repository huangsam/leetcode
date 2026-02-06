// https://leetcode.com/problems/set-matrix-zeroes/

public class SetMatrixZeroes {
    /**
     * Set entire row and column to zero if an element is zero.
     *
     * <p>We do an initial scan for all zeros. Whenever we spot a
     * zero in the matrix, we take stock of its row and its column.
     * Once we have the set of all rows and columns that need to be
     * zeroed out, then we actually do the operations.
     *
     * <p>The primary way to resort to O(1) memory usage is by
     * using the top row and left column to collect all columns
     * and rows where a zero was encountered. That way, we do not
     * need to have two {@link java.util.HashSet} instances for tracking
     * these occurrences.
     *
     * <p>Complexity:
     *
     * <ul>
     *     <li>Time: O(m * n)</li>
     *     <li>Space: O(1)</li>
     * </ul>
     */
    public void setZeroes(int[][] matrix) {
        int height = matrix.length;
        int width = matrix[0].length;

        boolean leftSet = false;
        for (int i = 0; i < height; i++) {
            leftSet |= matrix[i][0] == 0;
        }

        boolean topSet = false;
        for (int i = 0; i < width; i++) {
            topSet |= matrix[0][i] == 0;
        }

        // Scan for zeros, using left and top as notes
        for (int i = 1; i < height; i++) {
            for (int j = 1; j < width; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        // Set zeros in the middle
        for (int i = 1; i < height; i++) {
            for (int j = 1; j < width; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        if (leftSet) {
            for (int i = 0; i < height; i++) {
                matrix[i][0] = 0;
            }
        }

        if (topSet) {
            for (int i = 0; i < width; i++) {
                matrix[0][i] = 0;
            }
        }
    }
}
