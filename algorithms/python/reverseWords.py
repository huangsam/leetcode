class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = ""
        for word in s.split():
            string += word[::-1] + " "
        return string.strip()
