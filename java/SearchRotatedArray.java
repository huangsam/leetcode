// https://leetcode.com/problems/search-in-rotated-sorted-array/

public class SearchRotatedArray {
    public int search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        if (nums[lo] > nums[hi]) {
            int pivot = findPivot(nums);
            if (nums[pivot] < target) {
                return -1;
            }
            if (nums[pivot] == target) {
                return pivot;
            }
            if (nums[lo] <= target) { // search target in [lo, pivot)
                hi = pivot - 1;
            } else { // search target in (pivot, hi]
                lo = pivot + 1;
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
            if (nums[mid] < nums[lo]) { // pivot lies in first half
                hi = mid - 1;
            } else { // pivot lies in second half
                lo = mid + 1;
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
