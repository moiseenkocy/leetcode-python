"""Solution for problem #13 Roman to Integer.

https://leetcode.com/problems/roman-to-integer/
"""

class Solution:
    """Container class for storing solution."""

    def romanToInt(self, s: str) -> int:
        """Solve problem #13 Roman to Integer."""
        roman_digits = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        result = 0
        buf = s

        for x in (4, 9, 40, 90, 400, 900):
            roman_digit = roman_digits[x]
            if roman_digit in buf:
                buf = buf.replace(roman_digit, "")
                result += x

        for x in (1, 5, 10, 50, 100, 500, 1000):
            result += buf.count(roman_digits[x]) * x

        return result
