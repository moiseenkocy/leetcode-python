"""Tests for problem #9 Palindrome Number."""

import pytest

from leetcode_solutions.p0009_palindrome_number import Solution


@pytest.mark.parametrize(
    ("x", "expected_result"),
    [
        (121, True),
        (-121, False),
        (10, False),
    ],
)
def test_isPalindrome(x: int, expected_result: bool) -> None:
    """Test isPalindrome solution."""
    solver = Solution()

    result = solver.isPalindrome(x)

    assert result == expected_result
