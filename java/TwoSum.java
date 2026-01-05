// https://leetcode.com/problems/two-sum/

import java.util.HashMap;

public class TwoSum {
    /**
     * Time: O(n)
     * Space: O(n)
     *
     * We create a mapping of the numbers we have seen so far. While
     * we do this, we also check if the complement of the current
     * number (i.e., target - nums[i]) exists in the map. If it
     * does, we return the indices of the two numbers that add up to
     * the target.
     */
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seenValues = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seenValues.containsKey(complement)) {
                return new int[]{seenValues.get(complement), i};
            }
            seenValues.put(nums[i], i);
        }
        throw new IllegalArgumentException("This should not happen");
    }
}
