import collections


class Solution:
    @staticmethod
    def canConstruct(ransom_note: str, magazine: str) -> bool:
        ransom_dict = collections.Counter(ransom_note)
        magazine_dict = collections.Counter(magazine)
        for key, value in ransom_dict.items():
            if value > magazine_dict[key]:
                return False
        return True
