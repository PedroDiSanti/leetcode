from typing import List


class Solution:
    @staticmethod
    def removeDuplicates(nums: List[int]) -> int:
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)
