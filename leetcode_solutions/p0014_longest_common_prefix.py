"""Solution for problem #14 Longest Common Prefix.

https://leetcode.com/problems/longest-common-prefix/
"""


class Solution:
    """Container class for storing solution."""

    def longestCommonPrefix(self, strs: list[str]) -> str:
        """Solve problem #14 Longest Common Prefix."""
        answer = ""

        for i in range(min(map(str.__len__, strs))):
            if len({x[i] for x in strs}) != 1:
                break
            answer += strs[0][i]

        return answer
