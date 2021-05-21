class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = list()
        
        for point in points:
            distance = point[0]**2 + point[1]**2
            distances.append((distance, point))
            
        distances.sort()
        
        l = len(distances)
        res = []
        
        for _, point in distances[:k]:
            res.append(point)
            
        return res
            