from typing import List

"""
I need to verify if a prerequisite of a course
also have a prerequisite from the course in question,
building a infinite loop.

obs: it is needed to check the prerequisites over
all dependencies, this means dependencies of
dependencies

[1, 3, 4] [3, 2, 4] [4, 2] [2, 1]


"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        black_list = {}

        for req in prerequisites:
            current_req = req[1:]
            head = req[0]
            for dep in current_req:
                black_list.setdefault(dep, []).append(head)

            if len(set(current_req).intersection(set(black_list.setdefault(head, [])))) > 0:
                return False
            else:
                tmp_list = black_list[head].copy()
                while tmp_list:
                    item = tmp_list.pop(0)
                    if len(set(current_req).intersection(set(black_list.setdefault(item, [])))) > 0:
                        return False
                    tmp_list.extend(black_list.setdefault(item, []))
        return True


if __name__ == "__main__":
    # Tests cases
    s = Solution()
    print(s.canFinish(2, [[1, 0], [0, 1]]))
    print(s.canFinish(3, [[1, 0], [2, 0], [0, 2]]))
    print(s.canFinish(3, [[1, 0], [0, 2], [2, 1]]))
    print(s.canFinish(4, [[0, 1], [2, 3], [1, 2], [3, 0]]))
    print(s.canFinish(7, [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]))
    print(s.canFinish(20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]))
