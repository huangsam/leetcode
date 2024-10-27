// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LetterCombinations {
    private static final String[] LETTERS = {"", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) {
            return Arrays.asList();
        }
        List<String> result = new ArrayList<>();
        helper(digits, 0, new StringBuilder(), result);
        return result;
    }

    private void helper(String digits, int index, StringBuilder builder, List<String> result) {
        if (index == digits.length()) {
            result.add(builder.toString());
            return;
        }
        char[] letters = LETTERS[(int) (digits.charAt(index) - '0') - 1].toCharArray();
        for (char letter : letters) {
            builder.append(letter);
            helper(digits, index + 1, builder, result);
            builder.deleteCharAt(builder.length() - 1);
        }
    }
}
