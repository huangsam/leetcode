// https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

import java.util.Arrays;
import java.util.Comparator;

public class MinimumArrows {
    /**
     * Return the minimum number of arrows that must be shot to burst all balloons.
     *
     * Usually for interval problems, we sort by start time to merge
     * intervals in an orderly fashion. However, for this problem we
     * are sorting by end time, because we are counting the number
     * of non-overlapping intervals based on {@code previous.end}
     * and {@code current.start}. When we encounter an overlap based
     * on these two fields, we increment the count by one. Check out
     * these inputs to get an intuition.
     *
     * <pre>
     * 1,6 -> 2,8 -> 7,12 -> 10,16 (min 2)
     * 1,2 -> 3,4 -> 5,6 -> 7,8 (min 4)
     * 2,4 -> 4,6 -> 7,8 -> 1,10 (min 2)
     * </pre>
     *
     * <p>Complexity:
     *
     * <ul>
     *     <li>Time: O(n * log(n))</li>
     *     <li>Space: O(1)</li>
     * </ul>
     */
    public int findMinArrowShots(int[][] points) {
        // Sort by end time
        Arrays.sort(points, Comparator.comparingInt(a -> a[1]));

        int count = 1;
        int previousEnd = points[0][1];

        // Count the number of non-overlapping intervals
        for (int i = 1; i < points.length; i++) {
            if (points[i][0] > previousEnd) {
                count++;
                previousEnd = points[i][1];
            }
        }

        return count;
    }
}
