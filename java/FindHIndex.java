// https://leetcode.com/problems/h-index/

public class FindHIndex {
    /**
     * Computes the h-index of a researcher given an array of their paper citations.
     * The h-index is the maximum value h such that the researcher has at least h papers
     * cited at least h times.
     *
     * <p> The algorithm uses a frequency array to count papers with specific citation counts.
     * The array size is `citations.length + 1` to group citations exceeding the total
     * number of papers into the last bin.
     *
     * <p> After building the frequency array, the algorithm iterates from the highest
     * possible h-index down to 1. It keeps a running `sum` of papers with at least
     * the current index `i` citations. If `i` is less than or equal to `sum`, the
     * h-index is `i`. The first such `i` encountered is the maximum h-index.
     *
     * <p> If no valid `i` is found (e.g., no paper has at least 1 citation), the h-index is 0.
     *
     * <p>Complexity:
     * <ul>
     *     <li>Time: O(n)</li>
     *     <li>Space: O(n)</li>
     * </ul>
     */
    public int hIndex(int[] citations) {
        // Values of h-index are [0, citations.length]
        int[] frequency = new int[citations.length + 1];
        for (int paper : citations) {
            // We do not need precise frequencies after the last paper
            int index = Math.min(citations.length, paper);
            frequency[index]++;
        }

        // Go from right to left to find the maximum h-index
        int sum = 0;
        for (int i = frequency.length - 1; i > 0; i--) {
            sum += frequency[i];
            if (i <= sum) {
                return i;
            }
        }
        return 0;
    }
}
