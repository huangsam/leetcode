// https://leetcode.com/problems/set-matrix-zeroes/

import java.util.HashSet;
import java.util.Set;

public class SetMatrixZeroes {
    /**
     * We do an initial scan for all zeroes. Whenever we spot a
     * zero in the matrix, we take stock of its row and its
     * column in set-like structures. Once we have the set of
     * all rows and columns that need to be zeroed out, then
     * we actually do the operations as it were.
     */
    public void setZeroes(int[][] matrix) {
        Set<Integer> zeroRows = new HashSet<>();
        Set<Integer> zeroCols = new HashSet<>();
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    zeroRows.add(i);
                    zeroCols.add(j);
                }
            }
        }
        zeroRows.forEach(row -> {
            for (int col = 0; col < matrix[0].length; col++) {
                matrix[row][col] = 0;
            }
        });
        zeroCols.forEach(col -> {
            for (int row = 0; row < matrix.length; row++) {
                matrix[row][col] = 0;
            }
        });
    }
}
