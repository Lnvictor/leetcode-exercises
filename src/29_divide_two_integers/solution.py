"""
Integer division: Iterative solution
"""


class Solution:
    def divide(self, dividend: int, divisor: int):
        is_negative = not((dividend >= 0 and divisor >= 0) or (dividend < 0 and divisor < 0))
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend

        dividend = abs(dividend)
        divisor = abs(divisor)
        tmp_result = 0
        counter = 0
        while tmp_result <= dividend:
            tmp_result += divisor
            counter += 1

        result = (counter - 1)
        return -result if is_negative else result
