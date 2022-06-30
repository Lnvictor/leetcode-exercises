from ast import Try
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        occurrences_mapping = {}
        limit = len(nums)
        i = 0

        while True:
            try:
                if occurrences_mapping[nums[i]] < 2:
                    occurrences_mapping[nums[i]] += 1
                    i += 1
                    continue
                nums.pop(i)
            except KeyError:
                occurrences_mapping[nums[i]] = 1
                i += 1
            except IndexError:
                break

        return len(nums)


if __name__ == "__main__":
    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
