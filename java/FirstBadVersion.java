// https://leetcode.com/problems/first-bad-version/

import helper.VersionControl;

public class FirstBadVersion extends VersionControl {
    /**
     * Identify first bad version. Assume that all versions after a
     * bad version are also bad.
     *
     * <p>Complexity:
     *
     * <ul>
     *     <li>Time: O(log(n))</li>
     *     <li>Space: O(1)</li>
     * </ul>
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
