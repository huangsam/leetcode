# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Each letter in pattern maps to exactly one unique word in s.
        Each unique word in s maps to exactly one letter in pattern.
        No two letters map to the same word.
        No two words map to the same letter.
        """
        # Keep track of mappings
        letter_to_word = {}
        word_to_letter = {}

        words = s.split(" ")

        # Abort if there are leftover letters or words
        if len(pattern) != len(words):
            return False

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

        letters_mapped, words_mapped = set(), set()

        # Look for the same letter being mapped multiple times
        for letter in word_to_letter.values():
            if letter in letters_mapped:
                return False
            letters_mapped.add(letter)

        # Look for the same word being mapped multiple times
        for word in letter_to_word.values():
            if word in words_mapped:
                return False
            words_mapped.add(word)

        return True
