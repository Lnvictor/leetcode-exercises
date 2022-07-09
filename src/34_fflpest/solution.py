"""
Binary Search approach
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int):
        left_index = 0
        right_index = len(nums) - 1

        middle_index = right_index // 2

        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2
            if nums[middle_index] == target:
                return self._resolve(nums[left_index: right_index + 1], target, left_index, right_index)

            if nums[middle_index] > target:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1

        return [-1, -1]

    def _resolve(self, nums, target, left_index, right_index):
        resp = [-1, -1]
        for i, num in enumerate(nums):
            if num == target:
                resp[0] = i + left_index
                break

        for i, num in enumerate(reversed(nums)):
            if num == target:
                resp[1] = right_index - i
                break

        if any([item == -1 for item in resp]):
            resp = [max(resp), max(resp)]
        return resp


if __name__ == '__main__':
    s = Solution()
    # print(s.searchRange([5,7,7,7,8, 8, 810], 8))
    # print(s.searchRange([5,7,7,8,8,10], 6))
    # print(s.searchRange([], 6))
    print(s.searchRange([1], 1))
