from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1
        current_index = 0
        current_jump_length = nums[0]

        while current_index <= last_index:
            current_index += current_jump_length
            if current_index == last_index:
                return True

            current_jump_length = nums[current_index]

        return False


if __name__ == "__main__":
    s = Solution()
    s.canJump([2, 3, 1, 1, 4])
