from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int):
        seen = {}
        for i, num in enumerate(nums):
            index = seen.get(num, -1 * (i + k + 1))
            if i - index <= k:
                print(i, index, num)
                return True
            else:
                seen[num] = i

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))
    # print(s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
