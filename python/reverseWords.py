# https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverse the order of words in a string.

        To reverse the words in a string while keeping the words themselves intact,
        we first reverse the entire string, which places the words in reverse order
        but with each word's characters also reversed. Then, we split the string
        into words, and reverse each word back to its original form. Finally,
        we join the corrected words with spaces to form the result.

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        reversed_words = []

        # Process all tokens in reverse order
        for rev_word in s.strip()[::-1].split():
            # Each token can be reversed to get the word
            reversed_words.append(rev_word[::-1])

        # Join all words as a single string
        return " ".join(reversed_words)
