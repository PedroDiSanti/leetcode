class Solution:
    @staticmethod
    def romanToInt(s: str) -> int:
        roman_to_int_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
                             'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        count = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i + 2] in roman_to_int_dict:
                count += roman_to_int_dict[s[i:i + 2]]
                i += 2
            else:
                count += roman_to_int_dict[s[i]]
                i += 1
        return count
