"""Tests for problem #20 Valid Parentheses."""

import pytest

from leetcode_solutions.p0020_valid_parentheses import Solution


@pytest.mark.parametrize(
    ("s", "expected_result"),
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
    ],
)
def test_isValid(s: str, expected_result: bool) -> None:
    """Test isValid solution."""
    solver = Solution()

    result = solver.isValid(s)

    assert result == expected_result
