class Solution:
    def areOccurrencesEqual(self, s: str):
        counter = s.count(s[0])
        for letter in set(s):
            if s.count(letter) != counter:
                return False
        return True
