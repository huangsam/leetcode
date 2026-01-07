// https://leetcode.com/problems/zigzag-conversion/

public class ZigZagConversion {
    /**
     * Here are the steps to convert the string:
     *
     * <ul>
     *     <li>Set up an array of StringBuilder with numRows elements</li>
     *     <li>Iterate through string and append each character to its depth row</li>
     *     <li>Change direction when reaching the top or bottom row</li>
     *     <li>Concatenate all rows to get the final result</li>
     * </ul>
     *
     * <p>Complexity:
     *
     * <ul>
     *     <li>Time: O(n)</li>
     *     <li>Space: O(n)</li>
     * </ul>
     */
    public String convert(String s, int numRows) {
        if (numRows == 1) {
            return s; // No zigzag conversion needed
        }

        StringBuilder[] rows = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            rows[i] = new StringBuilder();
        }

        int depth = 0;
        int direction = 1; // 1 for going down, -1 for going up

        for (char ch : s.toCharArray()) {
            rows[depth].append(ch);

            // Change direction only when hitting actual boundaries
            if (depth == 0) {
                direction = 1;  // At top, must go down
            } else if (depth == numRows - 1) {
                direction = -1; // At bottom, must go up
            }

            depth += direction;
        }

        StringBuilder result = new StringBuilder();
        for (StringBuilder rowBuilder : rows) {
            result.append(rowBuilder);
        }

        return result.toString();
    }
}
