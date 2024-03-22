"""Solution for problem #27 Remove Element.

https://leetcode.com/problems/remove-element/
"""

class Solution:
    """Container class for storing solution."""

    def removeElement(self, nums: list[int], val: int) -> int:
        """Solve problem #27 Remove Element."""
        offset = 0

        for i in range(len(nums)):
            if nums[i] == val:
                offset += 1
                continue
            if offset:
                nums[i - offset] = nums[i]

        return len(nums) - offset