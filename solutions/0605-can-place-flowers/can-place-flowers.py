# Can Place Flowers (Easy)
# https://leetcode.com/problems/can-place-flowers/
# Accepted 2026-04-26 — Python3, runtime 8 ms, memory 19.6 MB
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        count = 0
        m = len(flowerbed)

        for i in range(m):
            if flowerbed[i] == 0:
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                right_empty = (i == m - 1 or flowerbed[i + 1] == 0)

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    count += 1

                    if count >= n:
                        return True

        return count >= n
