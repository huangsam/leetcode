// https://leetcode.com/problems/longest-consecutive-sequence/

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class LongestConsecutive {
    public int longestConsecutive(int[] nums) {
        int result = 0;

        Set<Integer> allNums = new HashSet<>();
        Arrays.stream(nums).forEach(allNums::add);

        for (int num : nums) {
            if (allNums.contains(num)) {
                int currentLength = 1;
                int lower = num - 1, higher = num + 1;

                while (allNums.contains(lower)) {
                    currentLength++;
                    allNums.remove(lower--); // avoid duplicate traversals
                }

                while (allNums.contains(higher)) {
                    currentLength++;
                    allNums.remove(higher++); // avoid duplicate traversals
                }

                result = Math.max(result, currentLength);
            }
        }

        return result;
    }
}
