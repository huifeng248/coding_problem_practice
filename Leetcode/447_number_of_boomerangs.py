class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:

# use map to keep track of the number of boomerange for each iteration, thus the map need to be cleared for the next iteration
# distance means delta x square + delta y square
        res = 0
        map = {}
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                d = self.get_distance(points[i], points[j])
                if d not in map:
                    map[d] = 0
                map[d] += 1
            
            for value in map.values():
                res += value * (value -1)
            
            map = {}
        
        return res

    def get_distance(self, a, b):
        x = a[0] - b[0]
        y = a[1] - b[1]
        return x**2 + y**2


# time O(n^2) n is the number of points. This is because the function uses a nested loop to iterate over all pairs of points, resulting in n * (n-1) iterations.
# space O(n) the space required to store the map HashMap. In the worst case, the map can contain n-1 keys, each with a value of n-1, which adds up to n * (n-1) entries. However, since the map is cleared at the end of each iteration, the maximum number of entries it can contain at any given time is n-1. Therefore, the space complexity of the function is O(n).
