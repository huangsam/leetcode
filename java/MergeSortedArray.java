// https://leetcode.com/problems/merge-sorted-array/

public class MergeSortedArray {
    /**
     * Assume that nums1 has m items and is m + n long. Assume that nums2
     * has n items and is n long. We know that m + n is >= 1 but either
     * m or n can have 0 items in the list. Given that nums1 is non-poulated
     * on the right hand side, it's a lot easier to do in-place sorting from
     * the right hand side, so we go ahead with that approach as it were.
     */
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (n == 0) {
            return;
        }
        int n1_index = m - 1;
        int n2_index = n - 1;
        int reverse = m + n - 1;
        while (n1_index >= 0 && n2_index >= 0) {
            if (nums1[n1_index] > nums2[n2_index]) {
                nums1[reverse--] = nums1[n1_index--];
            } else {
                nums1[reverse--] = nums2[n2_index--];
            }
        }
        while (n2_index >= 0) {
            nums1[reverse--] = nums2[n2_index--];
        }
    }
}
