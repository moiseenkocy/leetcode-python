"""Tests for problem #35 Search Insert Position."""

import pytest

from leetcode_solutions.p0035_search_insert_position import Solution


@pytest.mark.parametrize(
    ("nums", "target", "expected_result"),
    [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
    ],
)
def test_searchInsert(nums: list[int], target: int, expected_result: int) -> None:
    """Test searchInsert solution."""
    solver = Solution()

    result = solver.searchInsert(nums, target)

    assert result == expected_result
