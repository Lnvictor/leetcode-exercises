class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current_index = len(nums) -1
        while(current_index >= 0):
            values = [val for val in nums[current_index + 1:] if val > nums[current_index]]
            values.sort()
            if values:
                index = nums.index(values[0], current_index)
                self.swap(nums, current_index, index)
                nums[current_index + 1:] = sorted(nums[current_index + 1:])
                return
            current_index -= 1
            
        return nums.sort()
    
    def swap(self, nums, index1, index2):
        tmp = nums[index1]
        nums[index1] = nums[index2]
        nums[index2] = tmp
