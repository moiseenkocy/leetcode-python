"""Solution for problem #67 Add Binary.

https://leetcode.com/problems/add-binary/
"""


class Solution:
    """Container class for storing solution."""

    def addBinary(self, a: str, b: str) -> str:
        """Solve problem #67 Add Binary."""
        len_a = len(a)
        len_b = len(b)
        max_len = max(len_a, len_b)

        carry = 0
        result = ""

        for x, y in zip(
            a[::-1] + "0" * (max_len - len_a),
            b[::-1] + "0" * (max_len - len_b),
            strict=False,
        ):
            carry, digit = divmod(int(x) + int(y) + carry, 2)
            result += str(digit)
        if carry:
            result += "1"

        return result[::-1]
