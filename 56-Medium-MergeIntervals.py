class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        # ---First Solution---:


        # ---Second Solution---:
        intervals.sort(key = lambda k : k[0])
        ans = [intervals[0]]

        for newStart, newEnd in intervals[1::]:
            if newStart <= ans[-1][1]:
                ans[-1][1] = max(newEnd, ans[-1][1])
            else:
                ans.append([newStart, newEnd])
        
        return ans

# ---TEST---
intervals1 = [[1,3],[2,6],[8,10],[15,18]]
intervals2 = [[1,4],[4,5]]

s = Solution()
print(s.merge(intervals1))
print(s.merge(intervals2))

