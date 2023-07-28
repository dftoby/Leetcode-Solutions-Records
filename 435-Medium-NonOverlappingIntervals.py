class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:

        # ---First Solution---:


        # ---Second Solution---:

        # Greedy Algorithm
        intervals.sort(key = lambda k : (k[0],k[1]))
        ans = 0

        prevEnd = intervals[0][1]
        
        for newStart, newEnd in intervals[1::]:
            if prevEnd <= newStart:
                prevEnd = newEnd
            else:
                ans += 1
                prevEnd = min(prevEnd,newEnd)
        return ans

# ---TEST---
intervals1 = [[1,2],[2,3],[3,4],[1,3]]
intervals2 = [[1,2],[1,2],[1,2]]
intervals3 = [[1,2],[2,3]]

s = Solution()
print(s.eraseOverlapIntervals(intervals1))#1
print(s.eraseOverlapIntervals(intervals2))#2
print(s.eraseOverlapIntervals(intervals3))#0
