"""Solution for problem #20 Valid Parentheses.

https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
    """Container class for storing solution."""

    def isValid(self, s: str) -> bool:
        """Solve problem #20 Valid Parentheses."""
        stack = []

        for c in s:
            if c in "[({":
                stack.append(c)
            else:
                if not stack:
                    return False
                pair = stack.pop()
                if c != {"{": "}", "[": "]", "(": ")"}.get(pair):
                    return False

        return not stack
