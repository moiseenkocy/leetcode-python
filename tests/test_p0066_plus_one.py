"""Tests for problem #66 Plus One."""

import pytest

from leetcode_solutions.p0066_plus_one import Solution


@pytest.mark.parametrize(
    ("digits", "expected_result"),
    [
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([9], [1, 0]),
    ],
)
def test_plusOne(digits: list[int], expected_result: list[int]) -> None:
    """Test plusOne solution."""
    solver = Solution()

    result = solver.plusOne(digits)

    assert result == expected_result
