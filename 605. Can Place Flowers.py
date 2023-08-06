"""
165 ms runtime beats 83.79%
16.8 MB memory beats 17.1%
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n > (len(flowerbed)+1)//2: return False
        i = 0
        while i < len(flowerbed) and n > 0:
            if flowerbed[i] == 1:
                i += 2
            elif i == len(flowerbed)-1:
                if flowerbed[i-1] == 0:
                    n -= 1
                i += 1
            elif flowerbed[i+1] == 1:
                i += 3
            elif i == 0 or flowerbed[i-1] == 0:
                n -= 1
                i += 2
            else:
                i += 1
        return n == 0
