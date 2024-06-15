from collections import defaultdict

class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        ratios = defaultdict(int)
        result = 0
        
        for i in rectangles:
            ratio = i[0] / i[1]
            result += ratios.get(ratio, 0)
            ratios[ratio] += 1
        
        return result

s = Solution()

rectangles1 = [[4,8],[3,6],[10,20],[15,30]]
rectangles2 = [[4,5],[7,8]]

print(s.interchangeableRectangles(rectangles1))
print(s.interchangeableRectangles(rectangles2))