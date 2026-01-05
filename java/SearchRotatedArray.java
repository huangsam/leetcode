// https://leetcode.com/problems/search-in-rotated-sorted-array/

public class SearchRotatedArray {

    /**
     * Time: O(log(n))
     * Space: O(1)
     */
    public int search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        if (nums[lo] > nums[hi]) {
            int pivot = findPivot(nums);
            if (nums[pivot] == target) {
                return pivot;
            }
            if (nums[lo] <= target) {
                hi = pivot - 1; // Search target in [lo, pivot)
            } else {
                lo = pivot + 1; // Search target in (pivot, hi]
            }
        }
        return binarySearch(nums, target, lo, hi);
    }

    private int findPivot(int[] nums) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (mid < hi && nums[mid] > nums[mid + 1]) {
                return mid;
            }
            if (mid > lo && nums[mid] < nums[mid - 1]) {
                return mid - 1;
            }
            if (nums[mid] < nums[lo]) {
                hi = mid - 1; // Pivot lies in lower half
            } else {
                lo = mid + 1; // Pivot lies in upper half
            }
        }
        return -1;
    }

    private int binarySearch(int[] nums, int target, int lo, int hi) {
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return -1;
    }
}
