class Solution(object):
    def lengthOfLastWord(self, s):        
        str__ = s.split()
        
        if str__ == []:
            return 0
        return len(str__[len(str__) - 1])