from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def removeDuplicates(nums: List[int]) -> int:
        count = Counter(nums)
        added_count = Counter()
        insert_idx = 0

        for x in nums:
            if added_count[x] < 2:
                nums[insert_idx] = x
                insert_idx += 1
                added_count[x] += 1

        del nums[insert_idx:]
        return len(nums)
