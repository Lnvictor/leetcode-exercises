from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        new_matrix = []
        for i, v in enumerate(mat):
            new_matrix.append([])
            for y, p in enumerate(v):
                new_matrix[i].append(self.crazy_sum(mat=mat, i=i, j=y, k=k))

        return new_matrix

    def crazy_sum(self, mat: List[List[int]], i: int, j: int, k: int):
        start_i = i - k if i >= k else 0
        end_i = i + k

        start_j = j - k if j >= k else 0
        end_j = j + k
        sum = 0

        for o in range(start_i, end_i + 1):
            for p in range(start_j, end_j + 1):
                try:
                    val = mat[o][p]
                    sum += val
                except Exception:
                    break

        return sum


if __name__ == '__main__':
    s = Solution()
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    print(s.matrixBlockSum(mat=mat, k=1))
    # print(s.crazy_sum(mat=mat, i=0, j=0, k=1))
