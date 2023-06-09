from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        sorted_arr = sorted(set(arr), reverse=True)
        counter = 0
        sum = 0

        for el in sorted_arr:
            if (len(arr) - counter) < k:
                sum += (len(arr) - counter) * el
                counter += (len(arr) - counter)
                break

            count = arr.count(el)
            if count > 1:
                index_1 = arr.index(el)
                index_2 = arr.index(el, index_1 + 1)

                if (index_2 - index_1) < k:
                    sum += el * k
                    sum += el * (len(arr[index_2: index_2 + k]))
                    counter += (k + len(arr[index_2: index_2 + k]))
                    continue

            for _ in range(count):
                sum += el * k
                counter += k

        return sum


if __name__ == '__main__':
    s = Solution()
    # print(s.maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3))
    print(s.maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4))
