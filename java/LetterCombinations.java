public class LetterCombinations {
    private static final String[] digitToLetters = {"", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) {
            return Arrays.asList();
        }

        List<StringBuilder> builders = new ArrayList<>();

        char[] digitArray = digits.toCharArray();

        for (char letter : getLetters(digitArray[0])) {
            StringBuilder builder = new StringBuilder();
            builder.append(letter);
            builders.add(builder);
        }

        for (int i = 1; i < digitArray.length; i++) {
            List<StringBuilder> nextBuilders = new ArrayList<>();
            for (char letter : getLetters(digitArray[i])) {
                for (StringBuilder builder : builders) {
                    StringBuilder nextBuilder = new StringBuilder(builder.toString());
                    nextBuilder.append(letter);
                    nextBuilders.add(nextBuilder);
                }
            }
            builders = nextBuilders;
        }

        return builders.stream().map(sb -> sb.toString()).toList();
    }

    private char[] getLetters(char digit) {
        return digitToLetters[(int) (digit - '0') - 1].toCharArray();
    }
}
