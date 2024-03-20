"""Tests for problem #13 Roman to Integer."""

import pytest

from leetcode_solutions.p0013_roman_to_integer import Solution


@pytest.mark.parametrize(
    ("s", "expected_result"),
    [
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    ],
)
def test_romanToInt(s: str, expected_result: int) -> None:
    """Test romanToInt solution."""
    solver = Solution()

    result = solver.romanToInt(s)

    assert result == expected_result
