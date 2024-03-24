"""Tests for problem #67 Add binary."""

import pytest

from leetcode_solutions.p0067_add_binary import Solution


@pytest.mark.parametrize(
    ("a", "b", "expected_result"),
    [
        ("11", "1", "100"),
        ("1010", "1011", "10101"),
    ],
)
def test_addBinary(a: str, b: str, expected_result: str) -> None:
    """Test addBinary solution."""
    solver = Solution()

    result = solver.addBinary(a, b)

    assert result == expected_result
