// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

import container.TreeNode;

public final class SortedArrayToBST {
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length == 0) {
            return null;
        }
        TreeNode head = helper(nums, 0, nums.length - 1);
        return head;
    }

    public TreeNode helper(int[] nums, int low, int high) {
        if (low > high) {
            return null;
        }
        int mid = (low + high) / 2;
        return new TreeNode(
            nums[mid],
            helper(nums, low, mid - 1),
            helper(nums, mid + 1, high)
        );
    }
}
