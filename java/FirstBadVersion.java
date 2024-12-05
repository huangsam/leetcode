// https://leetcode.com/problems/first-bad-version/

import helper.VersionControl;

public class FirstBadVersion extends VersionControl {
    /**
     * Identify first bad version with. Assume that all versions
     * after a bad version are also bad. We keep checking all
     * items for a bad version with a binary search approach.
     *
     * <p> If a bad version exists, we look leftwards to see if there
     * are any other versions that are bad. Otherwise, we look
     * upwards to see for any existence of a bad version.
     *
     * <p> Whenever we find a bad version, we track the minimum found so far.
     * The minimum version is the first bad version.
     */
    public int firstBadVersion(int n) {
        int lo = 1, hi = n, first = n;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (isBadVersion(mid)) { // look down for earlier versions
                first = mid;
                hi = mid - 1;
            } else { // look up for newer versions
                lo = mid + 1;
            }
        }

        return first;
    }
}
