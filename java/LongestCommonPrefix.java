// https://leetcode.com/problems/longest-common-prefix/

public class LongestCommonPrefix {
    /**
     * Time: O(n * m)
     * Space: O(1)
     *
     * We first check if the array is empty or has only one element.
     * If that's not the case, we find the minimum length of all
     * the strings.
     * <p> We then iterate through the strings and compare the
     * characters at the same index. If they're the same, we append
     * the character to the prefix. If they're not, we return the
     * prefix. If we reach the end of the loop, we return the prefix.
     */
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }

        int minLength = strs[0].length();
        StringBuilder prefix = new StringBuilder();

        for (int i = 1; i < strs.length; i++) {
            minLength = Math.min(minLength, strs[i].length());
        }

        for (int i = 0; i < minLength; i++) {
            char currentChar = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j++) {
                if (currentChar != strs[j].charAt(i)) {
                    return prefix.toString();
                }
            }
            prefix.append(currentChar);
        }

        return prefix.toString();
    }
}
