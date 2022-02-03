class Solution:
    def reverseWords(self, s: str) -> str:
        tmp = s.split()
        new_str = ""
        
        for index, letter in enumerate(tmp[::-1]):
            new_str += letter
            if index < len(tmp) - 1:
                new_str += " "
            
        return new_str