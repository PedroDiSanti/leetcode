import re


class Solution:
    @staticmethod
    def isPalindrome(self, s: str) -> bool:
        new_string = re.sub("[^a-zA-Z0-9]", "", s).lower()
        len_string = len(new_string)
        if len_string == 0:
            return True

        i = 0
        j = len_string - 1
        while i != j or i >= j:
            if new_string[i] != new_string[j]:
                return False
            i += 1
            j -= 1
        return True

    @staticmethod
    def isPalindrome_with_slice(s: str) -> bool:
        new_string = re.sub("[^a-zA-Z0-9]", "", s).lower()
        return new_string == new_string[::-1]
