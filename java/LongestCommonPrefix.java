// https://leetcode.com/problems/longest-common-prefix/
public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        } else if (strs.length == 1) {
            return strs[0];
        }

        int minIndex = strs[0].length();
        int maxMatch = 0;

        for (int i = 1; i < strs.length; i++) {
            minIndex = Math.min(minIndex, strs[i].length());
        }

        while (maxMatch < minIndex) {
            boolean isBadMatch = false;
            char currentChar = strs[0].charAt(maxMatch);
            for (int i = 1; i < strs.length; i++) {
                if (currentChar != strs[i].charAt(maxMatch)) {
                    isBadMatch = true;
                    break;
                }
            }
            if (isBadMatch) {
                break;
            }
            maxMatch += 1;
        }

        return strs[0].substring(0, maxMatch);
    }
}
