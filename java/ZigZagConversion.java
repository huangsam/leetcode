// https://leetcode.com/problems/zigzag-conversion/
public final class ZigZagConversion {
    enum Direction {
        SOUTH,
        DIAGONAL
    }

    /**
     * Apply zigzag conversion:
     * PAYPALISHIRING -> PAHNAPLSIIGYIR
     *
     * Here are the things I'm thinking of.
     *
     * numRows = column size
     * numRows-2 = diagonal size
     *
     * So we want to understand how long the string is. Then we want
     * to go as follows:
     *
     * - Grab numRows chars
     * - Append to a mapping where key = rawIndex, value = list of chars
     * - Grab numRows-2
     * - Append to a mapping where key = rawIndex-1, value = list of chars
     * - If at any point we run out of characters, we stop the iteration
     */
    public String convert(String s, int numRows) {
        StringBuilder[] allRows = new StringBuilder[numRows];
        for (int depth = 0; depth < numRows; depth++) {
            allRows[depth] = new StringBuilder();
        }

        helper(s, numRows, allRows, Direction.SOUTH, 0);

        StringBuilder result = new StringBuilder();
        for (int depth = 0; depth < numRows; depth++) {
            result.append(allRows[depth].toString());
        }

        return result.toString();
    }

    public void helper(
        String s,
        int numRows,
        StringBuilder[] allRows,
        Direction direction,
        int absoluteIndex
    ) {
        int iterations = (direction == Direction.SOUTH)
            ? numRows : numRows - 2;

        for (int i = 0; i < iterations; i++) {
            if (absoluteIndex == s.length()) {
                return;
            }

            int depth = (direction == Direction.SOUTH)
                ? i : iterations - i;

            allRows[depth].append(s.charAt(absoluteIndex));

            absoluteIndex++;
        }

        Direction nextDirection = (direction == Direction.SOUTH)
            ? Direction.DIAGONAL : Direction.SOUTH;

        helper(s, numRows, allRows, nextDirection, absoluteIndex);
    }
}
