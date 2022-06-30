from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
		sorted_nums = sorted(nums)
		negative_numbers = [n for n in sorted_nums if n < 0]
		
