// https://leetcode.com/problems/product-of-array-except-self/

public class ProductExceptSelf {
    /**
     * Product of all the elements of nums except nums[i].
     *
     * What we need to do in this case is:
     * - Use cumulative product of left side without l-1
     * - Use cumulative product of right side without r+1
     * - Left product fills from left to right
     * - Right product fills from right to left
     *
     * [1, 2, 3, 4]
     * ->
     * [1, 1, 1, 1] (new array)
     * ->
     * [1, 1, 2, 6] (left transform)
     * ->
     * [24, 12, 4, 1] (right transform)
     * ->
     * [24, 12, 8, 6] (combined transform)
     */
    public int[] productExceptSelf(int[] nums) {
        int leftProduct = 1;
        int rightProduct = 1;

        int[] result = new int[nums.length];
        for (int i = 0; i < result.length; i++) {
            result[i] = 1;
        }

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
