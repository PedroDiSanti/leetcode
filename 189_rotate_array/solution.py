from typing import List


class Solution:
    @staticmethod
    def rotate(nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        if k != 0:
            nums[:] = nums[-k:] + nums[:-k]
