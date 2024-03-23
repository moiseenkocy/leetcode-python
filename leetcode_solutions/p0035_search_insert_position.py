"""Solution for problem #35 Search Insert Position.

https://leetcode.com/problems/search-insert-position/
"""


class Solution:
    """Container class for storing solution."""

    def searchInsert(self, nums: list[int], target: int) -> int:
        """Solve problem #35 Search Insert Position."""
        left = 0
        right = len(nums) - 1

        if nums[left] > target:
            return 0

        if nums[right] < target:
            return right + 1

        while right - left > 1:
            middle = left + (right - left) // 2
            value = nums[middle]

            if value > target:
                right = middle
            elif value < target:
                left = middle
            else:
                return middle

        return left if nums[left] == target else right