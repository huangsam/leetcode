// https://leetcode.com/problems/longest-common-prefix/
public class Solution {
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
            boolean badMatch = false;
            char currentChar = strs[0].charAt(maxMatch);
            for (int i = 1; i < strs.length; i++) {
                if (currentChar != strs[i].charAt(maxMatch)) {
                    badMatch = true;
                    break;
                }
            }
            if (badMatch == true) {
                break;
            }
            maxMatch += 1;
        }

        return strs[0].substring(0, maxMatch);
    }
}
