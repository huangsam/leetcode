// https://leetcode.com/problems/product-of-array-except-self/

import java.util.Arrays;

public class ProductExceptSelf {
    /**
     * Product of all the elements of {@code nums} except
     * {@code nums[i]}. What we need to do is:
     *
     * <ul>
     *     <li>Use cumulative product of left side without l-1</li>
     *     <li>Use cumulative product of right side without r+1</li>
     *     <li>Left product fills from left to right</li>
     *     <li>Right product fills from right to left</li>
     * </ul>
     *
     * Here is an example for demonstrative purposes:
     *
     * <pre>
     * [1, 2, 3, 4] (original)
     * [1, 1, 2, 6] (left transform)
     * [24, 12, 4, 1] (right transform)
     * [24, 12, 8, 6] (combined transform)
     * </pre>
     *
     * <p>Complexity:
     * <ul>
     *     <li>Time: O(n)</li>
     *     <li>Space: O(1)</li>
     * </ul>
     */
    public int[] productExceptSelf(int[] nums) {
        int leftProduct = 1;
        int rightProduct = 1;

        int[] result = new int[nums.length];
        Arrays.fill(result, 1);

        // Apply left and right transforms together
        for (int l = 0, r = result.length - 1; l < result.length; l++, r--) {
            result[l] *= leftProduct;
            leftProduct *= nums[l];

            result[r] *= rightProduct;
            rightProduct *= nums[r];
        }

        return result;
    }
}
