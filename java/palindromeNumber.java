// https://leetcode.com/problems/palindrome-number/
public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int right = length(x) - 1;
        int left = 0;
        while (right > left) {
            int digit_one = digit(x, right);
            int digit_two = digit(x, left);
            if (digit_one != digit_two) {
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
            x /= 10;
            count += 1;
        }
        return count;
    }

    public int digit(int x, int index) {
        int divisor = 1;
        while (index != 0) {
            index -= 1;
            divisor *= 10;
        }
        return (x / divisor) % 10;
    }
}
