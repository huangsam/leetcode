// https://leetcode.com/problems/reverse-integer/
public class ReverseInteger {
    public static final int TEN = 10;

    public int reverse(int x) {
        int result = 0;
        int digit = 0;
        boolean isNegative = (x < 0);

        if (isNegative) {
            x *= -1;
        }

        while (true) {
            digit = x % TEN;
            result = (result * TEN) + digit;
            x /= TEN;
            if (x == 0) {
                break;
            }
        }

        if (result % TEN != digit % TEN) {
            return 0;
        }

        if (isNegative) {
            return -1 * result;
        }

        return result;
    }
}
