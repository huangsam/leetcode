// https://leetcode.com/problems/h-index/

public class FindHIndex {
    /**
     * Computes the h-index of a researcher given an array of their paper citations.
     * The h-index is defined as the maximum value h such that the researcher has
     * at least h papers that have each been cited at least h times.
     *
     * <p> The algorithm works by first creating a frequency array to count the number
     * of papers with a certain number of citations. The size of this array is
     * `citations.length + 1` to accommodate citation counts up to the total
     * number of papers. Citations greater than `citations.length` are counted
     * in the last bin, as their exact count beyond this threshold is not relevant
     * for determining the h-index.
     *
     * <p> After populating the frequency array, the algorithm iterates from right to
     * left (from the highest possible h-index down to 1). In each iteration, it
     * maintains a running `sum` of the number of papers with at least the current
     * index `i` citations. If at any point the current index `i` is less than or
     * equal to this `sum`, it means we have found an h-index of `i` (at least `i`
     * papers have `i` or more citations). Since we are iterating from the largest
     * possible value downwards, the first such `i` we encounter will be the maximum
     * h-index.
     *
     * <p> If the loop completes without finding such an `i` (meaning no paper has at
     * least 1 citation, or only one paper has 0 citations, etc.), the h-index is 0.
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
