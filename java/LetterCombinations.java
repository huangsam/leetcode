// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

import java.util.ArrayList;
import java.util.List;

public class LetterCombinations {
    private static final String[] LETTERS = {"", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};    /**
     * Time: O(4^n)
     * Space: O(n)
     *
     * We go through each digit in the input string and find the corresponding
     * letters. We use a recursive helper function to build combinations of
     * letters. If the input string is empty, we return an empty list.
     */
    public List<String> letterCombinations(String digits) {
        if (digits.isEmpty()) {
            return List.of();
        }
        List<String> result = new ArrayList<>();
        helper(digits, 0, new StringBuilder(), result);
        return result;
    }

    /**
     * We go through different letters associated with each digit. When
     * we add a new letter to the mix, we increment the index by one.
     * When we reach the end, we have a valid combo and record it in
     * the list of results. Assume that order does not matter.
     */
    private void helper(String digits, int index, StringBuilder builder, List<String> result) {
        if (index == digits.length()) {
            result.add(builder.toString());
            return;
        }
        char[] letters = LETTERS[digits.charAt(index) - '0' - 1].toCharArray();
        for (char letter : letters) {
            builder.append(letter);
            helper(digits, index + 1, builder, result);
            builder.deleteCharAt(builder.length() - 1);
        }
    }
}
