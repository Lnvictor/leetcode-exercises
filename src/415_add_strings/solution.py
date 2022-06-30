class Solution:
    def transform(self, number):
        """
        This converts an string to int
        """
        exp = len(number) - 1
        result = 0
        for digit in number:
            result += (ord(digit) - 48) * (10**exp)
            exp -= 1

        return result

    def addStrings(self, num1: str, num2: str) -> str:
        """
        Explicit solution
        """
        n1 = self.transform(num1)
        n2 = self.transform(num2)

        return str(n1 + n2)


if __name__ == "__main__":
    print(Solution().addStrings("11", "123"))
