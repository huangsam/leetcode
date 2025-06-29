// https://leetcode.com/problems/two-sum/

import java.util.HashMap;

public class TwoSum {
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
