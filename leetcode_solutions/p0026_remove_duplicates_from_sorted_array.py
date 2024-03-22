"""Solution for problem #26 Remove Duplicates from Sorted Array.

https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

class Solution:
    """Container class for storing solution."""

    def removeDuplicates(self, nums: list[int]) -> int:
        """Solve problem #26 Remove Duplicates from Sorted Array."""
        skipped = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                skipped += 1
            else:
                nums[i - skipped] = nums[i]

        return len(nums) - skipped
