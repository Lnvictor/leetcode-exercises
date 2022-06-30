from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        _sum = nums[0] + nums[1] + nums[len(nums) - 1]
        nums.sort()

        for i in range(0, len(nums) - 2):
            first_pointer = nums[i]
            second_pointer = nums[i + 1]

            while first_pointer < second_pointer:
                partial_sum = nums[i] + nums[first_pointer] + nums[second_pointer]

                if partial_sum > target:
                    second_pointer -= 1
                else:
                    first_pointer += 1

                if abs(target - _sum) > abs(target - partial_sum):
                    _sum = partial_sum

        return _sum


if __name__ == "__main__":
    # TestCase
    l = [-3, -2, -5, 3, -4]
    target = -1
    solution = Solution()
    solution.threeSumClosest(l, target)
