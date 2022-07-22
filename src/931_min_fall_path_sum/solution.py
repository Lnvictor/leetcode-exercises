from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]):
        min_sum = 11000
        n = len(matrix)
        memo = []
        for i in range(n):
            memo.append([])
            for k in range(n):
                memo[i].append(None)

        for i, item in enumerate(matrix[0]):
            min_sum = min(min_sum, self.solve(matrix, 0, i, memo))

        return min_sum

    def solve(self, matrix, line, column, memo):
        if column < 0 or column >= len(matrix):
            return 11000

        if line == (len(matrix) - 1):
            return matrix[line][column]

        if not (memo[line][column] is None):
            return memo[line][column]

        middle = self.solve(matrix, line + 1, column, memo)
        right = self.solve(matrix, line + 1, column + 1, memo)
        left = self.solve(matrix, line + 1, column - 1, memo)

        memo[line][column] = min(left, middle, right) + matrix[line][column]
        return memo[line][column]


if __name__ == '__main__':
    s = Solution()
    # print(s.minFallingPathSum([[-19,57],[-40,-5]]))
    print(s.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
