// https://leetcode.com/problems/number-of-islands/

import java.util.HashSet;
import java.util.Set;
import java.util.stream.Stream;

public class NumberOfIslands {
    public int numIslands(char[][] grid) {
        int result = 0;
        Set<Integer> visited = new HashSet<>();

        // Note that i stands for row, j stands for column
        for (int i = 0; i < rowCount(grid); i++) {
            for (int j = 0; j < colCount(grid); j++) {
                Integer key = visitIndex(i, j, colCount(grid));
                if (grid[i][j] != '1' || visited.contains(key)) {
                    continue;
                }
                traverseAndTrack(grid, i, j, visited);
                result++;
            }
        }

        return result;
    }

    private void traverseAndTrack(
            char[][] grid, int i, int j,
            Set<Integer> visited) {
        Integer key = visitIndex(i, j, colCount(grid));

        boolean isVisitedOrInvalid = Stream.of(
            visited.contains(key),
            i < 0 || i >= rowCount(grid),
            j < 0 || j >= colCount(grid))
            .anyMatch(cond -> cond);

        if (isVisitedOrInvalid || grid[i][j] == '0') {
            return;
        }

        // Mark as partially visited
        visited.add(key);

        // Traverse in all 4 directions
        traverseAndTrack(grid, i + 1, j, visited);
        traverseAndTrack(grid, i - 1, j, visited);
        traverseAndTrack(grid, i, j + 1, visited);
        traverseAndTrack(grid, i, j - 1, visited);
    }

    private Integer visitIndex(int m, int n, int rowSize) {
        return m * rowSize + n;
    }

    private int rowCount(char[][] grid) {
        return grid.length;
    }

    private int colCount(char[][] grid) {
        return grid[0].length;
    }
}
