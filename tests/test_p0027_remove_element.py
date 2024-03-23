"""Tests for problem #27 Remove Element."""

import pytest

from leetcode_solutions.p0027_remove_element import Solution


@pytest.mark.parametrize(
    ("nums", "val", "expected_result"),
    [
        ([3, 2, 2, 3], 3, (2, [2, 2])),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, (5, [0, 1, 4, 0, 3])),
    ],
)
def test_removeElement(
    nums: list[int],
    val: int,
    expected_result: tuple[int, list[int]],
) -> None:
    """Test removeElement solution."""
    solver = Solution()

    result = solver.removeElement(nums, val)

    assert result == expected_result[0]
    assert sorted(nums[:result]) == sorted(expected_result[1])
