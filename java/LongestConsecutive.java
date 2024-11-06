// https://leetcode.com/problems/longest-consecutive-sequence/

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.Stack;

public class LongestConsecutive {
    private Stack<int[]> intervals;

    public LongestConsecutive() {
        intervals = new Stack<>();
    }

    public int longestConsecutive(int[] nums) {
        int result = 0;

        Set<Integer> allNums = new HashSet<>();
        Arrays.stream(nums).forEach(allNums::add);

        for (int num : nums) {
            if (isInInterval(num)) {
                continue;
            }
            int lower = num, higher = num;
            while (allNums.contains(lower - 1)) {
                lower--;
            }
            while (allNums.contains(higher + 1)) {
                higher++;
            }
            if (bestLength() < higher - lower + 1) {
                updateInterval(lower, higher);
            }
        }
        return bestLength();
    }

    /** Avoid duplicate interval searches */
    private boolean isInInterval(int num) {
        for (int[] interval : intervals) {
            if (interval[0] <= num && num <= interval[1]) {
                return true;
            }
        }
        return false;
    }

    /** Get best length found so far */
    private int bestLength() {
        if (intervals.isEmpty()) {
            return 0;
        }
        int[] interval = intervals.peek();
        return interval[1] - interval[0] + 1;
    }

    /** Update interval so far */
    private void updateInterval(int left, int right) {
        intervals.push(new int[]{left, right});
    }
}
