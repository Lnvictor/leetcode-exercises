"""
I will store the 3 possible letter by number,
in order to make possible query when needed
in allusion to a db... X:))
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_mapping = {
            '2': ['a', 'b', 'c'], 
            '3': ['d', 'e', 'f'],  
            '4': ['g', 'h', 'i'],  
            '5': ['j', 'k', 'l'],  
            '6': ['m', 'n', 'o'],  
            '7': ['p', 'r', 's'],  
            '8': ['t', 'u', 'v'],  
            '9': ['w', 'x', 'y', 'z']
        }
        combinations = []
        for index, digit in enumerate(digits):
            if index == 0:
                [combinations.append(item) for item in letter_mapping[digit]]
            else:
                tmp_comb = []
                previous_length = len(combinations)
                for index, comb in enumerate(combinations):
                    for item in letter_mapping[digit]:
                        new_item = comb + item
                        tmp_comb.append(new_item)
                combinations = tmp_comb

        return combinations


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))
