"""
65 ms runtime beats 63.88%
16.3 MB memory beats 46.33%
"""
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row[:] = row[::-1]
            for i in range(len(row)):
                row[i] = 1-row[i]
        return image