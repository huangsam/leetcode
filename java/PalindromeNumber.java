// https://leetcode.com/problems/palindrome-number/
public final class PalindromeNumber {
    public static final int TEN = 10;

    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int right = length(x) - 1;
        int left = 0;
        while (right > left) {
            int digitOne = digit(x, right);
            int digitTwo = digit(x, left);
            if (digitOne != digitTwo) {
                return false;
            }
            right -= 1;
            left += 1;
        }
        return true;
    }

    public int length(int x) {
        int count = 0;
        while (x != 0) {
            x /= TEN;
            count += 1;
        }
        return count;
    }

    public int digit(int x, int index) {
        int divisor = 1;
        while (index != 0) {
            index -= 1;
            divisor *= TEN;
        }
        return (x / divisor) % TEN;
    }
}
