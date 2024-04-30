class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_of_string = list(s.split())
        return len(list(list_of_string[-1]))
