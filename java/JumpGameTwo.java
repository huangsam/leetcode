// https://leetcode.com/problems/jump-game-ii/

import java.util.Arrays;

public class JumpGameTwo {
    /**
     * Time: O(n)
     * Space: O(1)
     *
     * Approach with near-far intuition
     */
    public int jump(int[] nums) {
        int near = 0;
        int far = 0;
        int jumps = 0;

        while (far < nums.length - 1) {
            // Find the farthest point from [near, far]
            int farthest = 0;
            for (int i = near; i <= far; i++) {
                farthest = Math.max(farthest, i + nums[i]);
            }

            // Set near pointer to the next range
            near = far + 1;

            // Set far pointer to the farthest point
            far = farthest;

            jumps++;
        }

        return jumps;
    }

    /** Approach with dynamic programming */
    public int jumpDynamic(int[] nums) {
        int[] minJumps = new int[nums.length];
        Arrays.fill(minJumps, Integer.MAX_VALUE - 1);
        minJumps[nums.length - 1] = 0;
        for (int i = nums.length - 2; i >= 0; i--) {
            for (int j = 1; j <= nums[i] && i + j < nums.length; j++) {
                minJumps[i] = Math.min(minJumps[i], 1 + minJumps[i + j]);
            }
        }
        return minJumps[0];
    }
}
