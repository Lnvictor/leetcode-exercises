from typing import List


class Solution:
    def getSums(self, previous_row: List[int]):
        numbers = [1]
        for i in range(0, len(previous_row) - 1):
            numbers.append(previous_row[i] + previous_row[i + 1])

        numbers.append(1)
        return numbers

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        arr = [1, 1]

        for _ in range(2, rowIndex + 1):
            arr = self.getSums(arr)

        return arr


if __name__ == "__main__":
    print(Solution().getRow(4))
