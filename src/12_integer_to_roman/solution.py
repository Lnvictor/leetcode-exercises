class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Transforms an integer into Roman algarism
        """
        
        algarisms = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1:"I",
        }
        
        
        l =  self.floor_key(num, algarisms)
        
        if num == l:
            return algarisms[num]
        
        return algarisms[l] + self.intToRoman(num-l)
    
    def floor_key(self, num, d):
        if num in d:
          return num
        return max(k for k in d if k < num)
