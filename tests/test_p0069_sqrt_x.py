"""Tests for problem #69 Sqrt(x)."""

import pytest

from leetcode_solutions.p0069_sqrt_x import Solution


@pytest.mark.parametrize(
    ("x", "expected_result"),
    [
        (4, 2),
        (8, 2),
    ],
)
def test_mySqrt(x: int, expected_result: int) -> None:
    """Test mySqrt solution."""
    solver = Solution()

    result = solver.mySqrt(x)

    assert result == expected_result
