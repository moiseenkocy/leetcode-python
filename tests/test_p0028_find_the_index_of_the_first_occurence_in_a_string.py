"""Tests for problem #28 Find the Index of the First Occurence in a String."""

import pytest

from leetcode_solutions.p0028_find_the_index_of_the_first_occurence_in_a_string import (
    Solution,
)


@pytest.mark.parametrize(
    ("haystack", "needle", "expected_result"),
    [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
    ],
)
def test_strStr(
    haystack: str,
    needle: str,
    expected_result: int,
) -> None:
    """Test strStr solution."""
    solver = Solution()

    result = solver.strStr(haystack, needle)

    assert result == expected_result
