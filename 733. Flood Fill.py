"""
Runtime: 153 ms, faster than 61.33% of Python3 online submissions 
Memory Usage: 14.2 MB, less than 40.12% of Python3 online submissions
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        origin = image[sr][sc]
        seen = defaultdict(set)
                
        def flood(image, sr, sc, origin, color):
            if image[sr][sc] == origin and sc not in seen[sr]:
                image[sr][sc] = color
                seen[sr].add(sc)
                
                for d in {1,-1}:                    
                    if 0<= sr+d < len(image):
                        flood(image, sr+d, sc, origin, color)               
                    if 0<= sc+d < len(image[0]):
                        flood(image, sr, sc+d, origin, color)              
        flood(image, sr, sc, origin, color)
        return image
        
        
        
        