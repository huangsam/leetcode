// https://leetcode.com/problems/merge-sorted-array/

public class MergeSortedArray {
    /**
     * Assume that {@code nums1} has m items and is m + n long. Assume that
     * {@code nums2} has n items and is n long. We know that m + n is >= 1
     * but either m or n can have 0 items in the list. Given that {@code nums1}
     * is non-populated on the right hand side, it's easier to do in-place
     * sorting from the right hand side.
     *
     * <p>Complexity:
     * <ul>
     *     <li>Time: O(m + n)</li>
     *     <li>Space: O(1)</li>
     * </ul>
     */
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (n == 0) {
            return;
        }
        int firstIndex = m - 1;
        int secondIndex = n - 1;
        int mergeIndex = m + n - 1;
        while (secondIndex >= 0) {
            if (firstIndex >= 0 && nums1[firstIndex] > nums2[secondIndex]) {
                nums1[mergeIndex--] = nums1[firstIndex--];
            } else {
                nums1[mergeIndex--] = nums2[secondIndex--];
            }
        }
    }
}
