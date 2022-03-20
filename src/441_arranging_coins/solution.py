

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n < 1:
            return 0
        
        count = 0
        previous = 0
        rows = 0

        for i in range(1, n + 1):
            count += (previous + 1)
            previous = i

            if count <= n:
                rows += 1
            else:
                break
        
        return rows


if __name__ == "__main__":
    print(Solution().arrangeCoins(5))
