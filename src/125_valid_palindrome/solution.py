class Solution:
    def isPalindrome(self, s: str) -> bool:
        lers = [letter for letter in s if letter.isalnum()]
        reverse_lers = lers[::-1]
        
        #print(lers)
        for i in range(len(lers)):
            a = lers[i].lower()
            b = reverse_lers[i].lower()

            if a != b:
                return False

        return True