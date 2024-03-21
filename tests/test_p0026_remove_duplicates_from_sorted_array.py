"""Tests for problem #26 Remove Duplicates from Sorted Array."""

import pytest

from leetcode_solutions.p0026_remove_duplicates_from_sorted_array import Solution


@pytest.mark.parametrize(
    ("nums", "expected_result"),
    [
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
    ],
)
def test_removeDuplicates(nums: list[int], expected_result: int) -> None:
    """Test removeDuplicates solution."""
    solver = Solution()

    result = solver.removeDuplicates(nums)

    assert result == expected_result
