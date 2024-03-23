"""Solution for problem #9 Palindrome Number.

https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    """Container class for storing solution."""

    def isPalindrome(self, x: int) -> bool:
        """Solve problem #9 Palindrome Number."""
        return str(x) == str(x)[::-1]
