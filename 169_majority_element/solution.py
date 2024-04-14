from typing import List


class Solution:
    @staticmethod
    def majorityElement(nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums).most_common()
        return count[0][0]
