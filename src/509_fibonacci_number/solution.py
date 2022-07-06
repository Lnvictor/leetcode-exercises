class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1

        ls = [1, 1]
        index = 2

        while index < n:
            sum = ls[index - 1] + ls[index - 2]
            ls.append(sum)
            index += 1

        return ls[-1]


if __name__ == '__main__':
    n = 5
    s = Solution()
    s.fib(5)
