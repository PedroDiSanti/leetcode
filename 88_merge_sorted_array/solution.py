from typing import List


class Solution:
    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        del (nums1[m:(m + n)])
        nums1.extend(nums2)
        nums1.sort()
