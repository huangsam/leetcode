# https://leetcode.com/problems/word-pattern/


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Determine if a string follows a given pattern.


        Each letter in pattern maps to exactly one unique word in s.
        Each unique word in s maps to exactly one letter in pattern.
        No two letters map to the same word.
        No two words map to the same letter.

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        words = s.split(" ")

        # Abort if there are leftover letters or words
        if len(pattern) != len(words):
            return False

        # Keep track of mappings
        letter_to_word = {}
        word_to_letter = {}

        # Iterate between the overlapping letters and words
        for curr_letter, curr_word in zip(pattern, words):
            if curr_letter not in letter_to_word:
                letter_to_word[curr_letter] = curr_word
            elif letter_to_word[curr_letter] != curr_word:
                return False

            if curr_word not in word_to_letter:
                word_to_letter[curr_word] = curr_letter
            elif word_to_letter[curr_word] != curr_letter:
                return False

        return True
