import math
import ipdb


class Solution:
    def primePalindrome(self, n: int) -> int:
        tmp = n
        while True:
            if self.is_palindrome(tmp) and self.is_prime(tmp):
                return tmp
            tmp += 1

            if 10**7 < tmp < 10**8:
                tmp = 10**8

    def is_palindrome(self, number):
        str_number = str(number)

        return str_number[::-1] == str_number

    def is_prime(self, number):
        if number <= 2:
            return number == 2

        i = 2
        while i <= int(math.sqrt(number)):
            if number % i == 0:
                return False
            i += 1

        return True


if __name__ == "__main__":
    s = Solution()
    s.primePalindrome(9989900)
