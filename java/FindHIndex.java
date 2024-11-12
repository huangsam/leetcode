// https://leetcode.com/problems/h-index/

public class FindHIndex {
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
