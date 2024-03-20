"""Solution for problem #1 Two Sum.

https://leetcode.com/problems/two-sum/
"""

class Solution:
    """Container class for storing solution."""

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Solve problem #1 Two Sum."""
        indexes = sorted(range(len(nums)), key=lambda x: nums[x])

        left = 0
        right = len(nums) - 1

        while True:
            curr_sum = nums[indexes[left]] + nums[indexes[right]]
            if target == curr_sum:
                break
            if target > curr_sum:
                left += 1
            else:
                right -= 1

        return [indexes[left], indexes[right]]
