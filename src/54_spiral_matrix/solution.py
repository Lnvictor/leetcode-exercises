from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        result = list()

        if matrix:
            for value in matrix.pop(0):
                result.append(value)

        if matrix:
            for index, value in enumerate(matrix):
                if value:
                    result.append(value.pop(-1))
                else:
                    matrix.pop(index)

        if matrix:
            last = matrix.pop()
            for value in last[::-1]:
                result.append(value)

        if matrix:
            for value in reversed(matrix[1:]):
                if value:
                    result.append(value.pop(0))

        return result + self.spiralOrder(matrix)
