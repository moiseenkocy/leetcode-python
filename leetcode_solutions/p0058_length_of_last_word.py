"""Solution for problem #58 Length of Last Word.

https://leetcode.com/problems/length-of-last-word/
"""


class Solution:
    """Container class for storing solution."""

    def lengthOfLastWord(self, s: str) -> int:
        """Solve problem #58 Length of Last Word."""
        end = len(s) - 1
        while s[end] == " ":
            end -= 1

        begin = end
        while s[begin] != " " and begin >= 0:
            begin -= 1

        return end - begin
