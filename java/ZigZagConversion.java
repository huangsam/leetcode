// https://leetcode.com/problems/zigzag-conversion/

public class ZigZagConversion {
    /**
     * Here are the steps to convert the string:
     * - Set up an array of StringBuilder with numRows elements
     * - Iterate through string and append each character to its depth row
     * - Change direction when reaching the top or bottom row
     * - Concatenate all rows to get the final result
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
            depth += direction;

            if (depth == numRows - 1 || depth == 0) {
                direction *= -1;
            }
        }

        StringBuilder result = new StringBuilder();
        for (StringBuilder rowBuilder : rows) {
            result.append(rowBuilder);
        }

        return result.toString();
    }
}
