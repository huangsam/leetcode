// https://leetcode.com/problems/longest-consecutive-sequence/

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class LongestConsecutive {

    /**
     * Time: O(n)
     * Space: O(n)
     *
     * By using a set, we're able to tell if adjacent neighbors to a current
     * value exist in the dataset, just by doing {@code val-1} or {@code val+1}.
     * In those cases, we simply go up and down as much as possible until we
     * arrive at the lower end and the higher end. If our current length is
     * greater than the max seen so far, then we save the new result and
     * continue until the end of the {@code nums} array.
     */
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
                    allNums.remove(lower--);
                }

                while (allNums.contains(higher)) {
                    currentLength++;
                    allNums.remove(higher++);
                }

                result = Math.max(result, currentLength);
            }
        }

        return result;
    }
}
