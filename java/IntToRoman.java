// https://leetcode.com/problems/integer-to-roman/

public class IntToRoman {
    /**
     * Convert integer to Roman numeral.
     *
     * <p>We start by holding all the Roman mappings in an array along with
     * edge cases like 900, 400, etc. We then iterate through the array and
     * keep subtracting until we reach 0.
     *
     * <p>Complexity:
     *
     * <ul>
     *     <li>Time: O(1)</li>
     *     <li>Space: O(1)</li>
     * </ul>
     */
    public String intToRoman(int num) {
        Roman[] romans = new Roman[] {
            new Roman(1000, "M"), new Roman(900, "CM"),
            new Roman(500, "D"), new Roman(400, "CD"),
            new Roman(100, "C"), new Roman(90, "XC"),
            new Roman(50, "L"), new Roman(40, "XL"),
            new Roman(10, "X"), new Roman(9, "IX"),
            new Roman(5, "V"), new Roman(4, "IV"),
            new Roman(1, "I")
        };
        int pointer = 0;
        StringBuilder builder = new StringBuilder();
        while (num > 0) {
            Roman roman = romans[pointer];
            while (num >= roman.value()) {
                num -= roman.value();
                builder.append(roman.code());
            }
            pointer++;
        }
        return builder.toString();
    }

    private record Roman(int value, String code) {
    }
}
