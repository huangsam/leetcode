// https://leetcode.com/problems/gas-station/

public class GasStation {
    /**
     * Time: O(n)
     * Space: O(1)
     *
     * Return starting point for completing a circuit. Note
     * that the current gas and differences help us with determining
     * that start point more easily.
     * <pre>
     * gas = [1,2,3,4,5], cost = [3,4,5,1,2]
     * sum(gas) = 15, sum(cost) = 15
     * diff = [-2,-2,-2,3,3]
     *
     * gas = [2,3,4], cost = [3,4,3]
     * sum(gas) = 9, sum(cost) = 10
     * diff = [-1,-1,1]
     * </pre>
     */
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int totalDifference = 0;
        int currentGas = 0;
        int result = 0;
        for (int i = 0; i < gas.length; i++) {
            int difference = gas[i] - cost[i];
            totalDifference += difference;
            currentGas += difference;
            if (currentGas < 0) {
                currentGas = 0; // Reset currentGas gas
                result = i + 1; // Look for next starting point
            }
        }
        return (totalDifference < 0) ? -1 : result;
    }
}
