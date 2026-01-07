// https://leetcode.com/problems/reverse-integer/

public class ReverseInteger {
    private static final int INT_MAX = 2147483647; // 2^31 - 1
    private static final int INT_MIN = -2147483648; // -2^31

    /**
     * <p>Complexity:
     *
     * <ul>
     *     <li>Time: O(log(n))</li>
     *     <li>Space: O(1)</li>
     * </ul>
     */
    public int reverse(int x) {
        // Determine sign; work with positive 'x' for reversal
        // Handle MIN_INT explicitly as abs(MIN_INT) overflows 32-bit int
        if (x == INT_MIN) {
            return 0;
        }
        int sign = (x < 0) ? -1 : 1;
        x = Math.abs(x); // Use Math.abs for clarity, knowing MIN_INT is handled

        int reversedNum = 0; // Accumulator for the reversed number (positive)

        while (x != 0) {
            int digit = x % 10;

            // Overflow check BEFORE multiplication/addition
            // Prevents `reversedNum * 10 + digit` from wrapping around
            if (reversedNum > INT_MAX / 10 || (reversedNum == INT_MAX / 10 && digit > 7)) {
                return 0; // Overflow detected
            }

            reversedNum = reversedNum * 10 + digit;
            x /= 10;
        }

        // No overflow check needed since reversedNum <= INT_MAX
        return reversedNum * sign;
    }
}
