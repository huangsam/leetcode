// https://leetcode.com/problems/reverse-integer/

public class ReverseInteger {
    private static final int TEN = 10;

    public int reverse(int x) {
        int result = 0;
        int digit = 0;
        boolean isNegative = (x < 0);

        if (isNegative) {
            x *= -1;
        }

        do {
            digit = x % TEN;
            result = (result * TEN) + digit;
            x /= TEN;
        } while (x != 0);

        if (result % TEN != digit % TEN) {
            return 0; // Handle overflow and underflow cases
        }

        return isNegative ? -result : result;
    }
}
