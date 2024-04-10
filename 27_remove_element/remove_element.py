from typing import List


class Solution:
    @staticmethod
    def removeElement(nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]
        print(nums)
        return len(nums)
