// https://leetcode.com/problems/reverse-integer/
public class Solution {
    public int reverse(int x) {
        int result = 0;
        int digit = 0;
        boolean negative = (x < 0);

        if (negative == true) {
            x *= -1;
        }

        while (true) {
            digit = x % 10;
            result = (result * 10) + digit;
            x /= 10;
            if (x == 0) {
                break;
            }
        }

        if (result % 10 != digit % 10) {
            return 0;
        }

        if (negative == true) {
            return -1 * result;
        }

        return result;
    }
}
