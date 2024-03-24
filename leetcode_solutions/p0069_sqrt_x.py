"""Solution for problem #69 Sqrt(x).

https://leetcode.com/problems/sqrtx/
"""


class Solution:
    """Container class for storing solution."""

    def mySqrt(self, x: int) -> int:
        """Solve problem #69 Sqrt(x)."""
        left = 0
        right = 65536

        while right - left > 1:
            middle = left + (right - left) // 2
            if middle * middle == x:
                return middle
            if middle * middle > x:
                right = middle
            else:
                left = middle

        return left
