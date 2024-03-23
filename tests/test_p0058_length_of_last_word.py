"""Tests for problem #58 Length of Last Word."""

import pytest

from leetcode_solutions.p0058_length_of_last_word import Solution


@pytest.mark.parametrize(
    ("s", "expected_result"),
    [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
    ],
)
def test_lengthOfLastWord(s: str, expected_result: int) -> None:
    """Test lengthOfLastWord solution."""
    solver = Solution()

    result = solver.lengthOfLastWord(s)

    assert result == expected_result
