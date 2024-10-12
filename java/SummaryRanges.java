import java.util.ArrayList;
import java.util.List;

public final class SummaryRanges {
    /**
     * We want this:
     * [0,1,2,4,5,7] -> ["0->2","4->5","7"]
     *
     * In order to achieve this:
     * - Iterate through nums one by one
     * - When non-contiguous, append start->end to result
     * - Reset start marker and repeat the process
     * - After iteration, add last start->end and return result
     */
    public List<String> summaryRanges(int[] nums) {
        List<String> result = new ArrayList<>();

        if (nums.length == 0) {
            return result;
        }

        if (nums.length == 1) {
            result.add(new Integer(nums[0]).toString());
            return result;
        }

        int start = 0, end = 1;
        while (end < nums.length) {
            if (nums[end] > nums[end - 1] + 1) {
                result.add(build(nums[start], nums[end - 1]));
                start = end;
            }
            end++;
        }

        result.add(build(nums[start], nums[end - 1]));

        return result;
    }

    private String build(Integer left, Integer right) {
        return left.equals(right)
            ? left.toString()
            : left.toString() + "->" + right.toString();
    }
}
