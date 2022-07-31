from typing import List
from collections import deque


class Solution:
    def find_content_chilren(self, g: List[int], s: List[int]) -> int:
        go = deque(sorted(g))
        so = deque(sorted(s))

        result = 0
        g1 = -1

        while so and (go or g1 > 0):
            if g1 < 0:
                g1 = go.popleft()

            s1 = so.popleft()
            if s1 >= g1:
                g1 = -1
                result += 1

        return result

    def load_input(self):
        with open('./input.txt', 'r') as file:
            lines = file.readlines()
            return eval(lines[0]), eval(lines[1])


if __name__ == '__main__':
    """
    TestCases
    """
    s = Solution()
    g, so = s.load_input()
    # print(s.find_content_chilren([1, 2], [1, 2, 3]))
    # print(s.find_content_chilren([1, 2, 3], [1, 1]))
    print(s.find_content_chilren(g, so))
