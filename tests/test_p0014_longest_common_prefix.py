"""Tests for problem #14 Longest Common Prefix."""

import pytest

from leetcode_solutions.p0014_longest_common_prefix import Solution


@pytest.mark.parametrize(
    ("strs", "expected_result"),
    [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
    ],
)
def test_longestCommonPrefix(strs: list[str], expected_result: str) -> None:
    """Test longestCommonPrefix solution."""
    solver = Solution()

    result = solver.longestCommonPrefix(strs)

    assert result == expected_result
