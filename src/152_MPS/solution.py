from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        
        max_value = None
        for index, val in enumerate(nums[:-1]):
            if max_value is None or val > max_value:
                max_value = val
            helper = val
            for v in nums[index + 1 :]:
                helper *= v
                if max_value is None or helper > max_value:
                    max_value = helper
        
        
        return nums[-1] if nums[-1] > max_value else max_value
            