from typing import List
from ipdb import sset_trace


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sset_trace()
        result = []

        def bracket(leftcount, rightcount, n, pattern, result):
            sset_trace()
            if len(pattern) == 2 * n:
                result.append(pattern)
                return
            if leftcount < n:
                bracket(leftcount + 1, rightcount, n, pattern + "(", result)
            if rightcount < leftcount:
                bracket(leftcount, rightcount + 1, n, pattern + ")", result)

        bracket(0, 0, n, "", result)
        return result


if __name__ == "__main__":
    s = Solution()
    s.generateParenthesis(3)
